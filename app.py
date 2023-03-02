from flask import Flask


# create flask app
app = Flask(__name__)

# main file
if __name__ == '__main__':
    app.run()


# importing routes
from routes import base, spam_text