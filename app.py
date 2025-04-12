import streamlit as st
import pickle

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

st.set_page_config(page_title="Movie Recommender", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
    body {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stApp {
        background-color: #0d1117;
    }
    .stButton > button {
        background-color: #238636;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #2ea043;
    }
    .movie-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
        height: 100px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# UI
st.markdown("<h1 style='color:#58a6ff'>🎬 Movie Recommender</h1>", unsafe_allow_html=True)

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie", [""] + list(movie_list))  # Empty default

if st.button("Show Recommendations"):
    if selected_movie == "":
        st.warning("Please select a movie to get recommendations.")
    else:
        recommended_movie_names = recommend(selected_movie)
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.markdown(f"<div class='movie-card'>{recommended_movie_names[idx]}</div>", unsafe_allow_html=True)
