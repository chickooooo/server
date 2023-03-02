from app import app


# home route
@app.get("/")
def get_home():
    status_code = 200
    data = {
        'status_code': status_code,
        'message': 'success'
    }

    return data, status_code


# unknown route
@app.errorhandler(404)
def page_not_found(error):
    status_code = 404
    data = {
        'status_code': status_code,
        'message': 'not found'
    }

    return data, status_code
