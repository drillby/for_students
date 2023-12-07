from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/hello/<string:jmeno>", methods=["POST"])
def hello(jmeno):
    print(type(jmeno))
    return f"Ahoj {jmeno}"


@app.route("/number/<int:cislo>")
def number_i(cislo):
    print(type(cislo))
    return f"Ahoj"


@app.route("/number/<float:cislo>")
def number_f(cislo):
    print(type(cislo))
    return f"Ahoj"


@app.route("/number/<int:cislo>/<float:cislo2>")
def number(cislo, cislo2):
    return f"Zadaná číslo je {cislo} a {cislo2}"


@app.get("/get")
def get():
    return "GET"


@app.post("/post")
def post():
    return "POST"


@app.put("/put")
def put():
    return "PUT"


@app.delete("/delete")
def delete():
    return "DELETE"


if __name__ == "__main__":
    app.run(debug=True)
