import streamlit as st
import pandas as pd
import re
import string
import pickle
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("scholarship_dataset.csv")
    df.fillna('', inplace=True)
    return df

# Load vectorizer
@st.cache_resource
def load_vectorizer():
    with open("vectorizer.pkl", "rb") as f:
        return pickle.load(f)

# Preprocessing function
def simple_preprocess(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    filtered = [word for word in tokens if word not in ENGLISH_STOP_WORDS]
    return " ".join(filtered)

# Recommendation function
def recommend_scholarships(query, df, vectorizer, top_n=5):
    df['clean_description'] = df['description'].apply(simple_preprocess)
    tfidf_matrix = vectorizer.fit_transform(df['clean_description'])
    query_processed = simple_preprocess(query)
    query_vec = vectorizer.transform([query_processed])
    similarity = cosine_similarity(query_vec, tfidf_matrix)
    top_indices = similarity.argsort()[0][-top_n:][::-1]
    return df.iloc[top_indices][['title', 'description', 'location', 'course', 'category']]

# Streamlit UI
st.set_page_config(page_title="Scholarship Recommender", layout="wide")
st.title("🎓 Scholarship Recommendation System")
st.write("Describe your profile and get personalized scholarship recommendations!")

user_input = st.text_area("Your Query", placeholder="E.g., I am a female student from Kerala studying BSc.")

if st.button("Find Scholarships"):
    if not user_input.strip():
        st.warning("Please enter your details to get recommendations.")
    else:
        df = load_data()
        vectorizer = load_vectorizer()
        results = recommend_scholarships(user_input, df, vectorizer)

        if not results.empty:
            for _, row in results.iterrows():
                st.markdown(f"### {row['title']}")
                st.markdown(f"**Location:** {row['location']}  \n**Course:** {row['course']}  \n**Category:** {row['category']}")
                st.markdown(f"{row['description']}")
                st.markdown("---")
        else:
            st.info("No scholarships found matching your query.")
