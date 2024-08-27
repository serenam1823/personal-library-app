# Personal Library App

## About

The purpose of this project is to create a more visual approach to keeping track of the books you read. With current popular book tracking platforms, like Goodreads, a user's reading journey is just comprised of different lists of their choosing, such as their "currently reading" and "want to read" lists. I wanted to create an application that serves this same purpose but displays these lists in a visual shelf format, similar to seeing shelves in a library. Users will be able to create shelves and add any books of their choosing to them, and they will show up as a collection of clickable shelves on the home screen, leading you to more information about these books once you click. Seeing a visual representation of your personal library is great for someone who doesn't have the space to display their books at home, reads e-books or audiobooks, or just wants to plan out their future home library. This application will also have the ablility to recommend new books to users based on the list of books that they have already read.

## Technologies Used

The primary technologies used in this application are React, Javascript, HTML/CSS, and Python. The frontend and backend of the application is connected with Flask.

### Recommendation Model

To create the recommendation feature for the application, I created a simple machine learning model that classifies books based on the features of its author, the average rating, number of ratings, and the genre. I based the learning of this model off of a dataset of books from Goodreads, which can be found [here](https://www.kaggle.com/datasets/middlelight/goodreadsbookswithgenres/data). I split this data into testing and training sets, and used the K Nearest Neighbors algorithm to create the model.
