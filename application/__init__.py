from flask import Flask
from flask_pymongo import PyMongo
# instance of Flask
app= Flask(__name__)
app.config['SECRET_KEY']='d93aebd2b32fdbeae363ac3a'
app.config['MONGO_URI']="mongodb+srv://ankita51523:<7WRwC3CPXmh5HHjB>@cluster0.gcgu6en.mongodb.net/?retryWrites=true&w=majority"

# setup mongodb
mongo_client= PyMongo(app)
db= mongo_client.db
from application import routes