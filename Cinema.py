from Movie import Movie
from imdb import Cinemagoer

def get_movie():
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
   
    user_rating = float(input("What would you rate this?\n> "))

    movie_object = Movie(movie["title"], movie["year"], movie["genres"], [str(movie["cast"][0]), str(movie["cast"][1])], movie["rating"], user_rating)
       
    return movie_object.get_dictionary()