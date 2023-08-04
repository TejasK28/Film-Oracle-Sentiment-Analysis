from Cinema import get_movie
from MongoDB import add_movie
from TestPrediction import predict

def prompt():
    print("[ 0 ] : ADD MOVIE TO DB\n[ 1 ] : PREDICT A MOVIE\n[ 2 ] : RECOMMEND A MOVIE")
    user_prompt = input("What do you want to do?\n> ")
    print()
    return user_prompt

def start():
    user_answer = int(prompt())
    if(user_answer == 0):
        add_movie(get_movie())
    if(user_answer == 1):
        predict(float(input("What is the imdb score of the movie?\n> ")))
    else: #Implement 
        print("I didn't implement that yet :<")


if __name__ == "__main__":
    start()
