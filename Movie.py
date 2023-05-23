class Movie:
    def __init__(self, title, year, genre, actors, rating, user_rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.actors = actors
        self.rating = rating
        self.user_rating = user_rating
    
    def get_dictionary(self):
        return {
        "name": self.title,
        "year": self.year,
        "genre" : self.genre,
        "actors" : self.actors,
        "imdb rating" : self.rating,
        "user rating" : self.user_rating
        }