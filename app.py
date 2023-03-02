from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/check")
def hello_world():
    # response = jsonify({'text': 'success!'})
    # response.headers.add(
    #     'Access-Control-Allow-Origin',
    #     'http://localhost:3000'
    # )
    # https://chickooo.netlify.app/
    return {'text': 'success!'}
