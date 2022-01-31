class Config:
    MOVIE_API__BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProductionConfig(Config):
    pass
class DevConfig(Config):
    Debug = True