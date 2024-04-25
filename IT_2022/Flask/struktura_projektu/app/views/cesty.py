from app import app

from flask import jsonify

@app.route("/")
def index():
    return "Hello World!"


@app.route("/cesta")
def cesta():
    objekt = {
        "klic1": "ahoj",
        "klic2": 123,
        "klic3": 3.1415,
        "pole": [1,2,3,4],
        "objekt" : {
            "klic11":"test",
        }
    }

    return jsonify(objekt)