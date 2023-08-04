import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from MongoDB import get_imdb_ratings, get_user_ratings

def train_linear_regression_model(X, y):
    # Initialize the linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(X, y)

    return model

def predict_user_rating(model, new_imdb_score):
    # Make predictions for the new IMDb score
    new_imdb_score = np.array(new_imdb_score).reshape(-1, 1)
    predicted_user_rating = model.predict(new_imdb_score)

    return predicted_user_rating[0]

def predict(score):
    # Sample data - replace these arrays with your actual data
    imdb_scores = np.array(get_imdb_ratings())
    user_ratings = np.array(get_user_ratings())

    # Prepare the data for training
    X = imdb_scores.reshape(-1, 1)
    y = user_ratings

    # Train the linear regression model
    model = train_linear_regression_model(X, y)

    # Test prediction with a new IMDb score
    new_imdb_score = score
    predicted_user_rating = predict_user_rating(model, new_imdb_score)

    print(f"Predicted User Rating for IMDb Score {new_imdb_score}: {predicted_user_rating:.2f}")
    if(predicted_user_rating > 7.0):
        print("Watch this movie!")
    else:
        print("Don't watch this movie!")
    


if __name__ == "__main__":
    # Sample data - replace these arrays with your actual data
    imdb_scores = np.array(get_imdb_ratings())
    user_ratings = np.array(get_user_ratings())

    # Prepare the data for training
    X = imdb_scores.reshape(-1, 1)
    y = user_ratings

    # Train the linear regression model
    model = train_linear_regression_model(X, y)

    # Test prediction with a new IMDb score
    new_imdb_score = 1
    predicted_user_rating = predict_user_rating(model, new_imdb_score)

    print(f"Predicted User Rating for IMDb Score {new_imdb_score}: {predicted_user_rating:.2f}")
    if(predicted_user_rating > 7.0):
        print("Watch this movie!")
    else:
        print("Don't watch this movie!")
