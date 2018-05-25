from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/createquote')
def createquote():
	return render_template('quote.html')

@app.route('/addquote', methods = ['POST', 'GET'])
def addquote():
    if request.method == 'POST':
      try:
         author = request.form['author']
         quote = request.form['quote']
         print()
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO quotes (author, quote) VALUES (?,?)",(author,quote) )
            
            con.commit()
            msg = "Quotations successfully added"
      except:
         con.rollback()
         msg = "Error in insert Quotations"
      
      finally:
         return render_template("result.html", msg = msg)
         con.close()

@app.route('/quotelist')
def quotelist():
	con = sql.connect('database.db')
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from quotes")

	rows = cur.fetchall()
	return render_template('quotelist.html', rows = rows)

if __name__ == '__main__':
	app.run(debug=True)