## 🎬 Movie Recommendation System (Content-Based)

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-green?logo=streamlit)](https://share.streamlit.io/)  

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
- **Streamlit Cloud:** [Click here to try the app](https://share.streamlit.io/)  
- **Heroku:** Deployed using `Procfile` and `setup.sh` (instructions in repo)  

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
| `Movie_Recommendation_System_Using_Machine_Learning_With_Python.ipynb` | Main Jupyter Notebook with model code |
| `movie_recommender.py` | Streamlit app for deployment |
| `trained_movie_model.sav` | Saved model (vectorizer + dataset) |
| `movies.csv` | Movie metadata dataset |
| `requirements.txt` | Python dependencies |
| `Procfile` & `setup.sh` | Heroku deployment files |
| `README.md` | Project documentation |

---

## 💡 Future Improvements
- Add a fully interactive **Streamlit web app**  
- Combine with user ratings for a **hybrid recommendation system**  
- Deploy online (e.g., **Render**, **HuggingFace**, or **Streamlit Cloud**)  

---

## 👨‍💻 Author
**Emmanuel Ogunkoya**  
📧 ogunkoyaemmanuel2024@gmail.com

Built as a fun machine learning project to explore **recommender systems**.  

⭐ Don’t forget to star this repo if you like it!
