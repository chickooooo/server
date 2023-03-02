from flask import Flask
import spacy
import os

try:
    # check if dependencies are present
    spacy.load("en_core_web_sm")
except:
    # install them if not present
    os.system('python -m spacy download en_core_web_sm')

# create flask app
app = Flask(__name__)

# main file
if __name__ == '__main__':
    app.run()


# importing routes
from routes import base, spam_text