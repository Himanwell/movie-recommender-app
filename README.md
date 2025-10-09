# 🎬 Movie Recommendation System (Content-Based)

This is a **content-based movie recommendation system** built using **Python** and **machine learning techniques**.  
It suggests movies similar to the one a user likes based on features like `genres`, `keywords`, `tagline`, `cast`, and `director`.

---

## ⚙️ Tech Stack

- **Python** 🐍
- **Pandas / NumPy** – Data handling
- **Scikit-learn** – TF-IDF Vectorizer + Cosine Similarity
- **Difflib** – Fuzzy title matching

---

## 🚀 How It Works

1. Combines key movie features
2. Converts them into numerical vectors using **TF-IDF Vectorizer**
3. Uses **cosine similarity** to measure how similar movies are
4. Returns the **top 10 most similar movies** to the one provided by the user

---

## 💡 Example

**Input:**
Enter your favourite movie name: iron man

**Output:**
Movies suggested for you:

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

If a movie title entered by the user isn’t found in the dataset, the system displays:
❌ Sorry, that movie is not in our database. Please try another one.

---

## 📂 Dataset

The system uses the **TMDB 5000 Movies Dataset**, which contains movie metadata such as:

- Movie titles
- Genres
- Keywords
- Tagline
- Cast
- Director

---

## 🧩 Project Files

| File                                                                   | Description                                         |
| ---------------------------------------------------------------------- | --------------------------------------------------- |
| `Movie_Recommendation_System_Using_Machine_Learning_With_Python.ipynb` | The main Jupyter Notebook containing the model code |
| `movies.csv`                                                           | The movie metadata dataset                          |
| `README.md`                                                            | Project documentation                               |

---

## 💡 Future Improvements

- Add a **Streamlit web app** for interactive recommendations
- Combine with **user ratings** for a hybrid recommendation system
- Deploy online (e.g., on **Render**, **HuggingFace**, or **Streamlit Cloud**)

---

## 👨‍💻 Author

**Emmanuel Ogunkoya**  
📧 *emmanuelogunkoya@gmail.com*  
Built as a fun machine learning project to explore recommender systems.

---

### ⭐ Don’t forget to star this repo if you like it!
