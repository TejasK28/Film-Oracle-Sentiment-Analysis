import pymongo
import tensorflow as tf

PASSWORD = open("password.txt", "r").read()

# Connect to the MongoDB database
client = pymongo.MongoClient(f"mongodb+srv://tejaskandri28:{PASSWORD}@cluster0.0hszhf8.mongodb.net/")
db = client["MovieDB"]

# Get all the movies from the database
movies = db.Movies.find()

# Print the movies
for movie in movies:
    print(movie)
    
