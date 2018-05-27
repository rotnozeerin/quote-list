import atexit
from flask import Flask, render_template, request
from utils import read_configuration
from storages import DatabaseBackend

app = Flask(__name__)

@app.route('/')
def quotelist():
    quotes = backend.list_quotes()
    return render_template('quote-list.html', rows=list(quotes))


@app.route('/create', methods = ['POST', 'GET'])
def create():
    if request.method == 'GET':
        return render_template('create-quote.html')

    elif request.method == 'POST':
      try:
         author = request.form['author']
         quote = request.form['quote']
           
         backend.add_quote({'quote':quote,'author':author})

         msg = "Quotations successfully added"
      except:
         msg = "Error in insert Quotations"
      
      finally:
         return render_template("result.html", msg=msg)
         
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':

    backend = DatabaseBackend()
    backend.on_start()
    atexit.register(backend.on_exit)
    
    config = read_configuration()
	hostname = config['hostname']
	port = int(config['port'])
	app.run(host=hostname, port=port, debug=True)