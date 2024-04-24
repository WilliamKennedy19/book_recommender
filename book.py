import numpy as np
import pandas as pd


books = pd.read_csv("Books.csv")
ratings = pd.read_csv("Ratings.csv")
users = pd.read_csv("Users.csv" )
print(books.head())