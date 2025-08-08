import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('Movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similar = pickle.load(open('similar.pkl', 'rb'))

def  recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similar[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title("Movie Recommendation")
selected = st.selectbox(
    "Enter the movie title",
    movies['title']
)
if st.button("Get Movie Recommendation"):
    for i in recommend(selected):
        st.write(i)
