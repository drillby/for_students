from faker import Faker
from flask import jsonify

from app import app, db

from ..models.models_11 import Profile, User

fake = Faker()


def user_to_dict(user):
    return {
        "id": user.id,
        "username": user.username,
        # Add other fields as necessary
    }


def profile_to_dict(profile):
    return {
        "id": profile.id,
        "bio": profile.bio,
        "user": user_to_dict(profile.user),
        # Add other fields as necessary
    }


@app.route("/generate_user")
def generate_user():
    user = User(username=fake.name())
    profile = Profile(bio=fake.text(), user=user)
    db.session.add(user)
    db.session.add(profile)
    db.session.commit()
    return jsonify(user_to_dict(user))


@app.route("/select_profiles")
def select_users():
    profiles = Profile.query.all()
    print(profiles[0].user)
    return jsonify([profile_to_dict(profile) for profile in profiles])
