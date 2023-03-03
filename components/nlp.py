from machine_learning.spam_text_class.setup import Setup


# setup the model and its dependencies
setup = Setup()


def post_spam_text_response(request):

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

    # if text is too long
    if len(body['text'].strip()) > 300:
        data['message'] = 'text is too long'
        return data, status_code

    # otherwise make predictions
    probability = setup.predict(body['text'])

    # update data
    status_code = 200
    data = {
        'status_code': status_code,
        'message': 'spam' if round(probability) == 1 else 'not spam',
        'confidence': round(probability, 2) if round(probability) == 1 else round(1-probability, 2)
    }

    return data, status_code
