from app import app
import requests
from .models import movies

movie = movies.Movie


API_KEY = app.config['MOVIE_API_KEY']
base_url = app.config['MOVIE_API__BASE_URL']


def get_movies(category):
    base_url_data = base_url.format(category, API_KEY)
    movies_data = requests.get(base_url_data).json()
    movie_data = []
    for data in movies_data['results']:
        id = data['id']
        title = data['title']
        overview = data['overview']
        poster = data['poster_path'] 
        vote_average = data['vote_average']
        vote_count = data['vote_count']
        movie_object = movie(id,title,overview,poster,vote_average,vote_count)
        movie_data.append(movie_object)

    return movie_data