from flask import Flask
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/api/recs')
def get_book_recs():
    books_df = pd.read_csv("./Goodreads_books_with_genres.csv")
    # print(books_df.info())

    # data cleanup
    books_df.dropna(subset=['genres'], inplace=True)
    books_df["genres"] = books_df["genres"].apply(lambda x: ';'.join( x.split(';')[:4] ).split(",")[0] )
    # print(books_df.head())

    genres_df = books_df["genres"].str.get_dummies(";")
    authors_df = books_df['Author'].str.get_dummies(",")

    # choose features and normalize them
    # features to look out for = genre, ratings, number of ratings, author ?
    scaler = StandardScaler()
    model_features = pd.concat([genres_df, authors_df, books_df['average_rating'], books_df['ratings_count'] ], axis = 1)
    features = scaler.fit_transform(model_features)

    #split data into testing and training data, on an 80-20 split
    X_train, X_test= train_test_split(features, test_size=0.2, random_state=np.random.randint(100))

    knn = NearestNeighbors()
    knn.fit(X_train)

    #call knn on your liked books?
    # knn.kneighbors(n_neighbors=5)

    return {"books": ['book1', 'book2', 'book3']}