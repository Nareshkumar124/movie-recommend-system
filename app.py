import streamlit as st
import pickle
import requests
# import pandas as pd
import os

if not (os.path.isfile("movies.pkl") and  os.path.isfile("movies.pkl")):
    from ml import convertIntoObject
    convertIntoObject()
    


url=""
imagePath:str=""
moviesList=pickle.load(open("movies.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
titles=moviesList["title"].values

def fetchPoster(id):
    formatedUrl:str=url.format(id)
    response=requests.get(formatedUrl)
    data=response.json()
    return f"{imagePath}{data['poster_path']}"
    # return "Under work"


def recommend(movie:str):
    movieIndex=moviesList[moviesList["title"]==movie].index[0]
    distances=similarity[movieIndex]
    sort=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1]) 
    topFive=sort[1:10] 
    # use enumerate to maintain the index and sort baed on index two value
    topFiveMoviesDf=moviesList.iloc[[index[0] for index in topFive]]


    movies=[]
    for _,movie in topFiveMoviesDf.iterrows():
        # posterPath=fetchPoster(movie.get("id"))
        movies.append(movie["title"])

    return movies

st.title("Movie Recommender System")

SelectedMovieName = st.selectbox(
    'Enter the name of the movie',
    titles)

if st.button("Recommend",type="primary"):
    recommendMovies=recommend(SelectedMovieName)
    for movie in recommendMovies:
        st.write(f"### {movie}")
        st.divider()





