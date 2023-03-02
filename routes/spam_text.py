from flask import request
from app import app


# spam text message classification
@app.post('/api/spam_text_class')
def post_spam_text():
    # default values
    status_code = 400
    data = {
        'status_code': status_code,
        'message': 'invalid request'
    }

    # getting json data
    body = request.get_json()

    # if text field not in body
    if 'text' not in body.keys():
        return data, status_code

    # if text is not string
    if not isinstance(body['text'], str):
        data['message'] = 'invalid datatype of {text}'
        return data, status_code

    # if text is too short
    if len(body['text'].strip()) < 5:
        data['message'] = 'text is too short'
        return data, status_code

    # otherwise
    # TODO: make prediction

    # update data
    status_code = 200
    data = {
        'status_code': status_code,
        'message': 'not spam',
        'confidence': 0.876
    }

    return data, status_code
