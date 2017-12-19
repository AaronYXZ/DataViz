from pymongo import MongoClient
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'projects'
COLLECTION_NAME = 'holiday'

FIELDS = {"date" : True,
        "type" : True,
        "locale" : True,
        "locale_name" : True,
        "description" : True,
        "transferred" : True,
        '_id': False}

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
collection = connection[DBS_NAME][COLLECTION_NAME]
holiday = collection.find(projection=FIELDS)
