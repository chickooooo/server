from flask import Flask, request
from flask_cors import CORS
from application.components import base, movie_review

# create flask app
app = Flask(__name__)
CORS(app)


# home route
@app.get("/")
def get_home():
    return base.get_home_response()


# unknown routes
@app.errorhandler(404)
def page_not_found(error):
    return base.get_404_response()


# movie review sentiment analysis
@app.post('/api/movie_review')
def post_movie_review():
    return movie_review.post_movie_review_response(request)


if __name__ == "__main__":
    app.run()
