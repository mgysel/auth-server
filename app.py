from flask import Flask, request
from json import dumps
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route('/')
def test():
    return "Hello World!!!"

#app.run(port='8090', debug=True)