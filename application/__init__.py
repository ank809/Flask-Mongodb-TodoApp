from flask import Flask
from flask_pymongo import PyMongo
from urllib.parse import quote_plus

# instance of Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd93aebd2b32fdbeae363ac3a'

username = "ankita51523"
password = "<THYME67@#a>"
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# app.config['MONGO_URI'] = f"mongodb+srv://{escaped_username}:
# {escaped_password}@cluster0.gcgu6en.mongodb.net/?retryWrites=true&w=majority"
app.config['MONGO_URI']="mongodb://localhost:27017/myDatabase"
# setup mongodb
mongo = PyMongo(app)
db = mongo.db

from application import routes
