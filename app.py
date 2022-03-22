from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

db = client.flask_db
todos = db.todos