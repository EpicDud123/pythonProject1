import pymongo
from datetime import datetime

# Replace these with your MongoDB connection details
mongo_url = "mongodb+srv://generalbai3:n9i6yp6BFH2cmwUz@cluster0.dlgwq8s.mongodb.net/"

# Create a MongoDB client
client = pymongo.MongoClient(mongo_url)

# Access a specific database
db = client["transate"]

# Access a specific collection within the database
collection = db["searchhistory"]

# Now you can perform operations on the collection, for example, inserting a document
document = {
    "ipaddress": "654.321",
    "text":"SANSSSSSSSSSSSS",
    "times":4,
    "result": "PAPYRUSSSSSSSSSSS",
    "utc_time": datetime.utcnow(),
}
result = collection.insert_one(document)

print(f"Inserted document with ID: {result.inserted_id}")

# Close the MongoDB connection
client.close()
