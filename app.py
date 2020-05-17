from flask import Flask, request
from json import dumps

app = Flask(__name__)

USER_DATA = []

class AccessError(HTTPException):
    code = 400
    message = 'No message specified'

class InputError(HTTPException):
    code = 400
    message = 'No message specified'

def defaultHandler(error):
    '''
    Handles flask errors
    '''
    response = error.get_response()
    print('response', error, error.get_response())
    response.data = dumps({
        "code": error.code,
        "name": "System Error",
        "message": error.get_description(),
    })
    response.content_type = 'application/json'
    return response
app.register_error_handler(Exception, defaultHandler)

@app.route('/signup', methods=['POST'])
def signup():
    user_info = request.get_json()

    user = {
        'email': user_info['email'],
        'password': user_info['password'] 
    }

    USER_DATA.append(user)

    # WHY IS THIS DONE? 
    # Must be to update the state, unnecessary if do not need
    return dumps(user)

@app.route('/login', methods=['POST'])
def login():
    user_info = request.get_json()

    user = {
        'email': user_info['email'],
        'password': user_info['password']
    }

    if (user in USER_DATA):
        return dumps(user)
    else:
        raise InputError('Email or Password is Invalid')

@app.route('/test', methods=['GET'])
def test():
    return "Hello World!!!"

app.run(port='8087', debug=True)