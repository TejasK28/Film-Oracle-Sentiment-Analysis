from Cinema import get_movie
from MongoDB import add_movie

dict_movie = get_movie()
add_movie(dict_movie)
