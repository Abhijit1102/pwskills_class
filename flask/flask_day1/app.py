from flask import Flask
from flask import request

app = Flask(__name__)
import requests

@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route("/1")
def hello_world1():
    return "Hello, world1!"

@app.route("/2")
def hello_world2():
    return "Hello, world2!"    

@app.route("/3")
def test():
    a = 5+6
    return f"sum : {a}"  

@app.route("/url")
def request_input():
    data = request.args.get('x') 
    return "this is my flask url {}".format(data)  


if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True)