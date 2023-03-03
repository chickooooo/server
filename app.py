from flask import Flask, request
from components import base, nlp

# create flask app
app = Flask(__name__)


# home route
@app.get("/")
def get_home():
    return base.get_home_response()


# unknown route
@app.errorhandler(404)
def page_not_found(error):
    return base.get_404_response()


# spam text message classification
@app.post('/api/spam_text_class')
def post_spam_text():
    return nlp.post_spam_text_response(request)


if __name__ == "__main__":
    app.run()
