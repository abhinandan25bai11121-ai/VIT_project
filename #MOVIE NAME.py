
import pandas as pd
import matplotlib as mp
import random as rand 


initializing = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
rec_data = []


#connecting csv file to program
df = pd.read_csv("top_100_movies.csv")
movie_name = df["title"].str.upper()
# print(movie_name)


selected_movie = movie_name.sample(n =100,replace= False)
# print(selected_movie)
for movie in selected_movie: # TANGLED
    for char in initializing: 
      if movie == " ":
          break
      if char in movie:# A , B, C
          a = movie.replace(char,"")
          count = count + 1
print(count)