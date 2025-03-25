from faker import Faker
from flask import jsonify

from app import app, db

from ..models.models_0 import Author

fake = Faker()


@app.route("/generate_data")
def generate_data():
    author = Author(name=fake.name())
    db.session.add(author)
    db.session.commit()

    return jsonify(author.name)


@app.route("/select_data")
def select_data():
    authors = Author.query.all()
    print(authors[0].id)
    print(authors[0].name)

    # Example selects
    """authors = Author.query.filter_by(name="Author 1").all()
    author_by_name = Author.query.filter_by(name="Author 1").first()
    authors_starting_with_a = Author.query.filter(Author.name.like("A%")).all()
    authors_ordered_by_name = Author.query.order_by(Author.name).all()"""

    return jsonify([author.name for author in authors])


@app.route("/delete_data")
def delete_data():
    author = Author.query.first()
    db.session.delete(author)
    db.session.commit()
    return jsonify(author.name if author else None)
