# 🎓 Scholarship Recommendation System

A **Streamlit-based web application** that recommends scholarships based on a user’s background and interests using **TF-IDF vectorization** and **cosine similarity**.

---

## 🚀 Overview

This project helps students find scholarships that best match their profile.  
Users simply describe themselves (for example: *"I’m a female student from Kerala studying BSc"*) and the app recommends the most relevant scholarships from a dataset.

---

## 🧠 Features

- 📝 **Natural language input** – users can describe their background in plain English.  
- 🧹 **Text preprocessing** – cleans and normalizes user input and scholarship descriptions.  
- 🤖 **Machine learning** – uses TF-IDF vectorization and cosine similarity for recommendations.  
- ⚡ **Streamlit UI** – simple, interactive, and responsive web interface.  
- 💾 **Caching** – optimized data and model loading using Streamlit’s caching decorators.

---

## 🗂️ Project Structure

scholarship-recommender/
│
├── scholarship_dataset.csv # Dataset containing scholarship information
├── vectorizer.pkl # Pre-trained TF-IDF vectorizer
├── app.py # Main Streamlit application
└── README.md # Project documentation



---

## 🧩 How It Works

### 🗃️ Data Loading
The app loads and cleans the scholarship dataset from a CSV file.

### 🔡 Text Vectorization
Each scholarship description is preprocessed (lowercased, punctuation removed, stopwords filtered).  
TF-IDF vectors are created using a pre-trained vectorizer (`vectorizer.pkl`).

### 📊 Similarity Computation
The user’s query is preprocessed and vectorized.  
Cosine similarity between the query vector and all scholarship descriptions is computed.

### 🏆 Top Recommendations
The app retrieves and displays the top N most similar scholarships with details such as title, location, course, category, and description.

---

📈 Future Enhancements

🧬 Integrate advanced models (e.g., BERT or Sentence Transformers) for better recommendations.

🌍 Add filters for country, degree level, or gender.

🔗 Connect to live scholarship APIs for real-time data.

🎨 Improve UI/UX with enhanced layout, search, and sorting features.
