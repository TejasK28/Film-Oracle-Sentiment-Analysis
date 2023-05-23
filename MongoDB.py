from pymongo import MongoClient
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://tejaskandri28:Kan29442@cluster0.0hszhf8.mongodb.net/")

# Get the database
db = client["MovieDB"]

# Get the collection
collection = db["Movies"]

# Create a document
movie = {
    "title": "The Shawshank Redemption",
    "year": 1994,
    "genre": "Drama",
    "rating": 9.3,
    "director": "Frank Darabont",
    "actors": ["Tim Robbins", "Morgan Freeman"]
}

# Insert the document
collection.insert_one(movie)

# Print the results
print(collection.find_one())