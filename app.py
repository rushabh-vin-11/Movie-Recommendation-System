import requests
import streamlit as st
import pickle
import pandas as pd

def fetch_poster(movie_id):
    requests.get('https://api.themoviedb.org/3/movie/1363?api_key=8265bd1679663z7ea12ac168da84d2e8&language=en-US')

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)    
    return recommended_movies    



similarity = pickle.load(open('similarity.pkl','rb'))

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie recommnder System')

option = st.selectbox(
    'How would you like to be contracted?',
    movies['title'].values
)

if st.button('Recommend'):
    recommendation = recommend(option)

    for i in recommendation:
        st.write(i)