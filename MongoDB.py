from pymongo import MongoClient
import pymongo
import tensorflow
from tensorflow import keras

PASSWORD = open("password.txt", "r").read()

# Connect to MongoDB
client = pymongo.MongoClient(
    f"mongodb+srv://tejaskandri28:{PASSWORD}@cluster0.0hszhf8.mongodb.net/")

# Get the database
db = client["MovieDB"]

# Get the collection
collection = db["Movies"]

# Create a document
movie = {
    "title": "Interstellar",
    "year": 2014,
    "genre": "Sci-Fi",
    "rating": 8.6,
    "director": "Christopher Nolan",
    "actors": ["Matthew McConaughey", "Anne Hathaway"],
    "user rating": 5
}

# Insert the document
collection.insert_one(movie)

# Print the results
print(collection.find)
