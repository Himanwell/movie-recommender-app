# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 20:13:23 2025

@author: Emmanuel
"""

# movie_recommender.py


import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches  # for fuzzy matching

# ------------------------
# Load the movie data
# ------------------------
# Replace this path with the actual path to your movies.csv
movies_data = pd.read_csv("C:\Users\Emmanuel\OneDrive\Desktop\MOVIE RECOMMENDATION SYSTEM\movies.csv")

# ------------------------
# Combine features for content-based filtering
# ------------------------
def combine_features(row):
    return str(row.get('genres', '')) + " " + str(row.get('keywords', '')) + " " + \
           str(row.get('cast', '')) + " " + str(row.get('director', ''))

movies_data["combined_features"] = movies_data.apply(combine_features, axis=1)

# ------------------------
# CountVectorizer & Cosine Similarity
# ------------------------
cv = CountVectorizer()
count_matrix = cv.fit_transform(movies_data["combined_features"])
similarity = cosine_similarity(count_matrix)

# ------------------------
# Recommendation function with fuzzy matching
# ------------------------
def recommend(movie_name):
    # Fuzzy match movie name
    all_titles = movies_data['title'].tolist()
    matches = get_close_matches(movie_name, all_titles, n=1, cutoff=0.6)
    if not matches:
        return ["Movie not found. Please check the spelling."]
    
    movie_name = matches[0]  # closest match
    movie_index = movies_data[movies_data.title == movie_name].index[0]
    
    similar_movies = list(enumerate(similarity[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:6]
    recommended = [movies_data.iloc[i[0]].title for i in sorted_similar_movies]
    return recommended

# ------------------------
# Streamlit interface
# ------------------------
st.title("🎬 Movie Recommendation System")

# User types the movie name
selected_movie = st.text_input("Type a movie you liked:")

if st.button("Show Recommendations"):
    if selected_movie.strip() == "":
        st.write("Please type a movie name.")
    else:
        recommendations = recommend(selected_movie)
        st.write("We recommend:")
        for movie in recommendations:
            st.write("• " + movie)

