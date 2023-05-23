from imdb import Cinemagoer
from Movie import Movie

# create an instance of the Cinemagoer class
ia = Cinemagoer()

movie_name = str(input("Enter movie name: "))

movies = ia.search_movie(movie_name)

counter = 0
try:
    for movie in movies:
        try:
            print("[",counter,"] : ", movie," ~ ", ia.get_movie(movie.movieID)["year"])
        except:
            print("[",counter,"] : ", movie," ~ ", "No Year Found")
        counter += 1
except:
    print("No movies found")

while(True):
    index_of_movie = int(input("Which one?\n> "))
    if(index_of_movie >= 0 and index_of_movie <= counter):
        break
    
movie = ia.get_movie(ia.search_movie(movie_name)[index_of_movie].movieID)

obj123 = Movie(movie["title"], movie["year"], movie["genres"], [str(movie["cast"][0]), str(movie["cast"][1])], movie["rating"], None)
print(obj123.get_dictionary())