from pymongo import MongoClient
import pymongo
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access the database
db = client['movies_db']

# Access the collection (or create it if it doesn't exist)
collection = db['movies']

# Movie details
movie = {
    'title': 'The Shawshank Redemption',
    'rating': 9.3
}

# Insert the movie into the collection
result = collection.insert_one(movie)

# Check if the insertion was successful
if result.acknowledged:
    print('Movie inserted successfully.')
    print('Inserted movie ID:', result.inserted_id)
else:
    print('Failed to insert the movie.')

# Close the MongoDB connection
client.close()
