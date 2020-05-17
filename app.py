from flask import Flask, request
from json import dumps
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "Hello World!!!"

#app.run(port='8089', debug=True)