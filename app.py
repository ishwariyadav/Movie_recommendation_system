import streamlit as st
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
import os
movies_data = pd.read_csv(os.path.join(os.path.dirname(__file__),'movies.csv'))

# Select features
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# Preprocess data
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

# Create feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Calculate similarity
similarity = cosine_similarity(feature_vectors)

# Streamlit app
st.title('Movie Recommendation System')

movie_name = st.text_input('Enter your favorite movie name:')

if st.button('Get Recommendations'):
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        
        st.write("Movies suggested:")
        for i, movie in enumerate(sorted_similar_movies[1:31], 1):
            index = movie[0]
            title_from_index = movies_data[movies_data.index == index]['title'].values[0]
            st.write(f"{i}. {title_from_index}")
    else:
        st.write("No close matches found. Please try another movie name.")