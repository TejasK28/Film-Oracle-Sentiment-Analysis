import requests
import json
from bs4 import BeautifulSoup

#Links
ROTTON_TOMATOES_MOVIES = "https://www.rottentomatoes.com/m/"

def get_new_movie():
    MOVIE_LINK = input("Enter the movie link:\n > ")
    request = requests.get(MOVIE_LINK)
    soup = BeautifulSoup(request.text, 'html.parser')
    print(soup.find("h1", class_="scoreboard__title").get_text(strip=True))


if __name__ == '__main__':
    get_new_movie()