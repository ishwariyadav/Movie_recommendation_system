def get_recommendations(movie_title):
    # Dummy data for demonstration
    movies = {
        'The Matrix': ['Inception', 'Blade Runner', 'The Terminator'],
        'Inception': ['Interstellar', 'Memento', 'The Prestige'],
        'Titanic': ['The Notebook', 'Romeo + Juliet', 'A Walk to Remember']
    }
    
    return movies.get(movie_title, ['No recommendations found'])
