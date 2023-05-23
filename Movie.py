
class Movie:
    def __init__(self, title, year, genre, tomatoRating, actors):
        self.title = title
        self.year = year
        self.genre = genre
        self.tomatoRating = tomatoRating
        self.actors = actors
    
    def get_dictionary(self):
        return {
        "name": self.title,
        "year": self.year
        }