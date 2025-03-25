from flask import Flask

from .models.models_MN import db

# from .models.models_11 import db

# from .models.models_login import db

# from .models.models_0 import db


# from .models.models_1N import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://student1:spsnet@dbs.spskladno.cz:3306/vyuka1"
)


db.init_app(app)

with app.app_context():
    db.create_all()


# from .views import views_0

# from .views import views_11

# from .views import views_1N

from .views import views_MN

# from .views import views_login


@app.route("/drop_all")
def drop_all():
    db.drop_all()
    return "Dropped all tables"
