import streamlit as st
import pickle
import os


class Recommed:
    def __init__(self) -> None:
        if not (os.path.isfile("movies.pkl") and  os.path.isfile("movies.pkl")):
            from ml import convertIntoObject
            convertIntoObject()
        self.load()
    
    def load(self):
        self.moviesList=pickle.load(open("movies.pkl","rb"))
        self.similarity=pickle.load(open("similarity.pkl","rb"))
        
    @property
    def titiles(self):
        return self.moviesList["title"].values
        
    def recommend(self,movie:str):
        movieIndex=self.moviesList[self.moviesList["title"]==movie].index[0]
        distances=self.similarity[movieIndex]
        sort=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1]) 
        topFive=sort[1:6] 
        topFiveMoviesDf=self.moviesList.iloc[[index[0] for index in topFive]]

        return topFiveMoviesDf['title']





object=Recommed()

st.title("Movie Recommender System")

SelectedMovieName = st.selectbox(
    'Enter the name of the movie',
    object.titiles)

if st.button("Recommend",type="primary"):
    recommendMovies=object.recommend(SelectedMovieName)
    for movie in recommendMovies:
        st.write(f"### {movie}")
        st.divider()





