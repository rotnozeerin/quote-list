from utils import read_configuration
import pymongo
from pymongo import MongoClient


def database_connection():
    config = read_configuration()
 
    mongo_hostname = config['mongo_hostname']
    mongo_port = int(config['mongo_port'])

    client = MongoClient(mongo_hostname, mongo_port)
    mongodb = client.QuoteData
    return mongodb