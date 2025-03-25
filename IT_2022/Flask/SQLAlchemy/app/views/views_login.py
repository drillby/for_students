from faker import Faker
from flask import jsonify

from app import app, db

from ..models.models_login import User

fake = Faker()


@app.route("/generate_data_login")
def generate_data_login():
    pw = fake.password()
    user = User(username=fake.user_name(), password=pw, email=fake.email())
    db.session.add(user)
    db.session.commit()

    return jsonify({"user": user.username, "password": pw})


@app.route("/register/<string:username>/<string:password>")
def register(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"})


@app.route("/login/<string:username>/<string:password>")
def login(username, password):
    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Login failed"})
