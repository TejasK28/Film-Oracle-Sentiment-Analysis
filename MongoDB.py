from pymongo import MongoClient
import pymongo

text = open("password.txt", "r").read()

# Connect to MongoDB
client = pymongo.MongoClient(f"mongodb+srv://tejaskandri28:{text}@cluster0.0hszhf8.mongodb.net/")

# Get the database
db = client["MovieDB"]

# Get the collection
collection = db["Movies"]

# Create a document
movie = {
    "title": "The Dark Knight",
        "year": 2008,
        "genre": "Action",
        "rating": 9.0,
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger"],
        "user rating": 8.0
}

# Insert the document
collection.insert_one(movie)

# Print the results
print(collection.find_one())