import streamlit as st
import pickle
import os
from api import posterPath

class Recommed:
    def __init__(self) -> None:
        if not (os.path.isfile("movies.pkl") and  os.path.isfile("movies.pkl")):
            from ml import convertIntoObject
            convertIntoObject()
        self.load()
    
    def load(self):
        self.moviesList=pickle.load(f1:=open("movies.pkl","rb"))
        self.similarity=pickle.load(f2:=open("similarity.pkl","rb"))
        f1.close()
        f2.close()
        
    @property
    def titiles(self):
        return self.moviesList["title"].values
        
    def recommend(self,movie:str):
        movieIndex=self.moviesList[self.moviesList["title"]==movie].index[0]
        distances=self.similarity[movieIndex]
        sort=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1]) 
        topFive=sort[1:6] 
        topFiveMoviesDf=self.moviesList.iloc[[index[0] for index in topFive]]
        
        #fetch poster
        movies=[]
        poster=[]
        for i in topFiveMoviesDf.iterrows():
            url=self.urlOfPoster(i[1]["id"])
            poster.append(url)
            movies.append(i[1]["title"])
        
        return zip(movies,poster)
            


    def urlOfPoster(self,movieId):
        path=posterPath(movieId)
        
        url=f"https://image.tmdb.org/t/p/original/{path}"
        
        return url




object=Recommed()

st.title("Movie Recommender System")

SelectedMovieName = st.selectbox(
    'Enter the name of the movie',
    object.titiles)

if st.button("Recommend",type="primary"):
    recommendMovies=object.recommend(SelectedMovieName)
    col1, col2, col3,col4 ,col5 = st.columns(5)
    recommendMovies=list(recommendMovies)
    with col1:
       # st.text(recommendMovies[0][0])
       st.image(recommendMovies[0][1],caption=f"{recommendMovies[0][0]}")
    with col2:
       # st.text(recommendMovies[1][0])
       st.image(recommendMovies[1][1],caption=f"{recommendMovies[1][0]}")
    with col3:
       # st.text(recommendMovies[2][0])
       st.image(recommendMovies[2][1],caption=f"{recommendMovies[2][0]}")
    with col4:
       # st.text(recommendMovies[3][0])
       st.image(recommendMovies[3][1],caption=f"{recommendMovies[3][0]}")
    with col5:
       # st.text(recommendMovies[4][0])
       st.image(recommendMovies[4][1],caption=f"{recommendMovies[4][0]}")





