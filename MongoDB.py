from pymongo import MongoClient
import pymongo
import tensorflow
from tensorflow import keras

PASSWORD = open("password.txt", "r").read()

def add_movie(dict_movie):
    # Connect to MongoDB
    client = pymongo.MongoClient(
        f"mongodb+srv://tejaskandri28:{PASSWORD}@cluster0.0hszhf8.mongodb.net/")

    # Get the database
    db = client["MovieDB"]

    # Get the collection
    collection = db["Movies"]

    # Insert the document
    collection.insert_one(dict_movie)

    # Print the results
    print(collection.find)

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
