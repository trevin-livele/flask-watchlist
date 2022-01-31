from app import app
from flask import render_template
from .request import get_movies


@app.route('/')
def index():
    data_link = get_movies('popular')
    return render_template('index.html',data_link=data_link)
