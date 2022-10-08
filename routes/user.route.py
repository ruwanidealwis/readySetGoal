from app import app, db


@app.route("/user")
def user():
    db.users.insert({"name": "Tink", "age": 22})
