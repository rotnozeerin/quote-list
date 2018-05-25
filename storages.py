import json
from connection import database_connection

class AbstractBackend:
    def list_quotes(self):
        raise NotImplemented

    def add_quote(self, quote):
        raise NotImplemented

    def on_start(self):
        pass


class InMemoryBackend(AbstractBackend):
    quotes = []

    def list_quotes(self):
        return self.quotes

    def add_quote(self, quote):
        self.quotes.append(quote)


class DatabaseBackend(AbstractBackend):

    db = None

    def on_start(self):
       self.db = database_connection()

    def list_quotes(self):
        rows = self.db.Quotes.find()
        return rows

    def add_quote(self, quote):
        self.db.Quotes.insert_one({
            'author':quote['author'],'quote': quote['quote']
        })