from flask import Flask


app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.get("/")
def hello_world():
    return {'text': 'success!'}
