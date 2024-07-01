from pymongo import MongoClient

client = MongoClient("mongodb://localhost:4000/")
db = client.mydatabase
collection = db.customers

for doc in collection.find():
    print(doc)
