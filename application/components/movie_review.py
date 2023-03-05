from domain.models.movie_review.setup import Setup


# setup the model and its dependencies
setup = Setup()


def post_movie_review_response(request):

    # default values
    status_code = 400
    data = {
        'status_code': status_code,
        'message': 'invalid request'
    }

    # getting json data
    body = request.get_json()

    try:
        # text field present
        assert 'text' in body.keys(), 'invalid request'
        # text is of type string
        assert isinstance(body['text'], str), 'invalid datatype of {text}'
        # min length of text is 5 characters
        assert len(body['text'].strip()) > 5, 'text is too short'
        # max length of text is 2,000 characters
        assert len(body['text'].strip()) < 2_000, 'text is too long'
    except Exception as e:
        data['message'] = str(e)
        return data, status_code

    # otherwise make predictions
    probability = setup.predict(body['text'])
    label = 'positive' if round(probability) == 1 else 'negative'
    confidence = round(probability, 2) if label == 'positive' else round(
        1-probability, 2)

    # update data
    status_code = 200
    data = {
        'status_code': status_code,
        'message': label,
        'confidence': str(confidence)
    }

    return data, status_code
