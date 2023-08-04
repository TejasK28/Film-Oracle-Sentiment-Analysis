from pymongo import MongoClient
import pymongo


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

    
def get_movies():
    # Connect to MongoDB
    client = pymongo.MongoClient(
        f"mongodb+srv://tejaskandri28:{PASSWORD}@cluster0.0hszhf8.mongodb.net/")

    # Get the database
    db = client["MovieDB"]

    # Get the collection
    collection = db["Movies"]

    # Retrieve all documents from the collection
    movies = collection.find()

    # You can loop through the results to access individual documents
    for movie in movies:
        print(movie)
    
    return movies

def get_imdb_ratings():
    # Connect to MongoDB
    client = pymongo.MongoClient(
        f"mongodb+srv://tejaskandri28:{PASSWORD}@cluster0.0hszhf8.mongodb.net/")

    # Get the database
    db = client["MovieDB"]

    # Get the collection
    collection = db["Movies"]

    # Retrieve all documents from the collection
    movies = collection.find()

    # Extract IMDb ratings and store them in a list
    imdb_ratings = []
    for movie in movies:
        imdb_ratings.append(movie.get("imdb rating"))

    return imdb_ratings

def get_user_ratings():
    # Connect to MongoDB
    client = pymongo.MongoClient(
        f"mongodb+srv://tejaskandri28:{PASSWORD}@cluster0.0hszhf8.mongodb.net/")

    # Get the database
    db = client["MovieDB"]

    # Get the collection
    collection = db["Movies"]

    # Retrieve all documents from the collection
    movies = collection.find()

    # Extract IMDb ratings and store them in a list
    user_ratings = []
    for movie in movies:
        user_ratings.append(movie.get("user rating"))
    return user_ratings
