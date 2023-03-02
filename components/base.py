
def get_home_response():
    status_code = 200
    data = {
        'status_code': status_code,
        'message': 'success'
    }

    return data, status_code


def get_404_response():
    status_code = 404
    data = {
        'status_code': status_code,
        'message': 'not found'
    }

    return data, status_code
