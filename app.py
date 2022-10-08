import ssl
from flask import Flask
from flask_pymongo import PyMongo
from pprint import pprint
import os

app = Flask(__name__)
# app.run(debug=True)
# app.config["MONGO_URI"] = os.getenv("DB_URI")
mongodb_client = PyMongo(app, uri="")
db = mongodb_client.db
pprint(vars(mongodb_client))


@app.route("/")
def home():
    users = db.users.find({"name": "Tink"})
    return users

@app.route("/user")
def user():
    # print(mongodb_client.db)
    mongodb_client.db.users.insert_one({"name": "Tink", "age": 22})
    return "Success"