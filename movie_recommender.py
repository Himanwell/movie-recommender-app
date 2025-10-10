# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 20:13:23 2025
@author: Emmanuel
"""

import os
import joblib
import streamlit as st
import pandas as pd
import difflib
import pickle
import requests
from io import BytesIO

# -------------------------------
# Load model and data safely
# -------------------------------



@st.cache_resource
def load_model():
    url = "https://huggingface.co/Himanwell/movie-recommender-app/blob/main/trained_model.sav"
    response = requests.get(url)
    model = pickle.load(BytesIO(response.content))
    return model


@st.cache_data
def load_movies_data():
    # Read the CSV file from local directory (must be in your repo)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "movies.csv")
    return pd.read_csv(data_path)

try:
    movie_model = load_model()
    movies_data = load_movies_data()
    st.success("✅ Model and data loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model or data: {e}")
    st.stop()

similarity = movie_model

# -------------------------------
# Streamlit App Interface
# -------------------------------

st.title("🎬 Movie Recommendation System")
st.write("Type the name of a movie you like, and I’ll suggest similar ones!")

movie_input = st.text_input("Enter movie title:", placeholder="e.g. Avatar")

if st.button("Recommend"):
    user_movie = movie_input.strip()

    if user_movie == "":
        st.warning("⚠️ Please enter a movie name.")
    else:
        try:
            list_of_all_titles = movies_data["title"].tolist()
            find_close_match = difflib.get_close_matches(user_movie, list_of_all_titles)

            if not find_close_match:
                st.error("❌ Sorry, that movie is not in our database. Please try another one.")
            else:
                close_match = find_close_match[0]
                index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
                similarity_score = list(enumerate(similarity[index_of_the_movie]))
                sorted_similar_movies = sorted(similarity_score, key=lambda x:x[1], reverse=True)

                st.write("🎥 **Movies suggested for you:**")
                for i, movie in enumerate(sorted_similar_movies[:10]):
                    index = movie[0]
                    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
                    st.write(f"{i+1}. {title_from_index}")

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

st.markdown("---")
st.caption("Created by Emmanuel • Powered by Streamlit 🚀")

