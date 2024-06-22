import pymongo

# Connect to MongoDB server
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or connect to a database
mydb = myclient["mydatabase"]

# Create or connect to a collection
mycollection = mydb["mycollection"]

# Insert a document into the collection
mydocument = { "name": "John", "address": "Highway 37" }
insert_result = mycollection.insert_one(mydocument)
print(f"Document inserted with _id: {insert_result.inserted_id}")

# Find one document in the collection
found_document = mycollection.find_one()
print(found_document)

# Find all documents in the collection
for doc in mycollection.find():
    print(doc)
