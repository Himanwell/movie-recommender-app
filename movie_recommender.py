# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 20:47:24 2025

@author: Emmanuel
"""

import streamlit as st
import pickle
import difflib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os

# ---------------------------------------------------------
# Set base directory to the folder where this script lives
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Full path to the saved model
model_path = os.path.join(BASE_DIR, 'trained_movie_model.sav')

# ---------------------------------------------------------
# Load the saved model
# ---------------------------------------------------------
with open(model_path, 'rb') as file:
    loaded_model = pickle.load(file)

vectorizer = loaded_model['vectorizer']
movies_data = loaded_model['movies_data']

# ---------------------------------------------------------
# Preprocess and rebuild combined features
# ---------------------------------------------------------
combined_features = (
    movies_data["genres"] + " " +
    movies_data["keywords"] + " " +
    movies_data["tagline"] + " " +
    movies_data["cast"] + " " +
    movies_data["director"] + " " +
    movies_data["original_title"]
)

# Convert text data into feature vectors
feature_vectors = vectorizer.transform(combined_features)

# Compute cosine similarity matrix
similarity = cosine_similarity(feature_vectors)

# ---------------------------------------------------------
# Streamlit App Interface
# ---------------------------------------------------------
st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favourite one!")

# Input movie name
movie_name = st.text_input("Enter your favourite movie name:")

if st.button("Recommend"):
    if movie_name.strip() == "":
        st.warning("⚠️ Please enter a movie name.")
    else:
        # List of all titles in the dataset
        list_of_all_titles = movies_data["title"].tolist()

        # Find close match for the entered movie
        find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

        if not find_close_match:
            st.error("❌ Sorry, that movie is not in our database. Try another one.")
        else:
            close_match = find_close_match[0]
            index_of_the_movie = movies_data[movies_data.title == close_match].index[0]

            # Get similarity scores for the selected movie
            similarity_score = list(enumerate(similarity[index_of_the_movie]))
            sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

            st.success(f"Movies similar to **{close_match}**:")
            for i, movie in enumerate(sorted_similar_movies[:10]):
                index = movie[0]
                title_from_index = movies_data.iloc[index]['title']
                st.write(f"{i+1}. 🎥 {title_from_index}")

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Scikit-learn")

st.caption("Made by Ogunkoya Emmanuel 🎬")

