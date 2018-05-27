import json
from connection import database_connection

class AbstractBackend:
    def list_quotes(self):
        raise NotImplemented

    def add_quote(self, quote):
        raise NotImplemented

    def on_start(self):
        pass

     def on_exit(self):
        pass

class InMemoryBackend(AbstractBackend):
    quotes = []

    def list_quotes(self):
        return self.quotes

    def add_quote(self, quote):
        self.quotes.append(quote)


class DatabaseBackend(AbstractBackend):

    db = None
    conn = None

    def on_start(self):
       self.conn = database_connection()
       self.db = self.conn.QuoteData
    
    def on_exit(self):
        self.conn.close()

    def list_quotes(self):
        rows = self.db.Quotes.find()
        return rows

    def add_quote(self, quote):
        self.db.Quotes.insert_one({
            'author':quote['author'],'quote': quote['quote']
        })