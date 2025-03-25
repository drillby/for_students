from faker import Faker
from flask import jsonify

from app import app, db

from ..models.models_1N import Article, Author

fake = Faker()


@app.route("/generate_data_1N")
def generate_data_1N():
    author = Author(name=fake.name())
    db.session.add(author)
    db.session.commit()

    article1 = Article(title=fake.word(), author_id=author.id)
    article2 = Article(title=fake.word(), author_id=author.id)
    db.session.add(article1)
    db.session.add(article2)
    db.session.commit()

    return jsonify(
        {"author": author.name, "articles": [article1.title, article2.title]}
    )


@app.route("/select_data_1N")
def select_data_1N():
    authors = Author.query.all()
    authors_list = [
        {
            "id": author.id,
            "name": author.name,
            "articles": [
                {"id": article.id, "title": article.title}
                for article in author.articles
            ],
        }
        for author in authors
    ]

    # Example selects
    """authors = Author.query.filter_by(name="Author 1").all()
    author_by_name = Author.query.filter_by(name="Author 1").first()
    authors_starting_with_a = Author.query.filter(Author.name.like("A%")).all()
    authors_ordered_by_name = Author.query.order_by(Author.name).all()"""

    return jsonify(authors_list)


@app.route("/delete_data_1N")
def delete_data_1N():
    author = Author.query.first()
    db.session.delete(author)
    db.session.commit()
    return jsonify(author.name if author else None)
