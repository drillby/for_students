from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1 style=color:red;>Hello, World!</h1>"


"""@app.route("/cesta")
def cesta():
    return "Jiný text"""


@app.route("/cesta/cesta2")
def cesta2():
    return "Uplně jiný text"


@app.route("/<string:promenna>")
def promenna(promenna):
    print(type(promenna))
    return f"Proměnná je {promenna} a datový typ je {type(promenna)}"


@app.route("/<int:promenna>")
def promenna2(promenna):
    print(type(promenna))
    return f"Proměnná je {promenna} a dato typ je {type(promenna)}"


if __name__ == "__main__":
    app.run(debug=True)
