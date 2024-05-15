from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:operace>/<int:cislo1>/<int:cislo2>")
def operace(operace, cislo1, cislo2):
    OPERACE = {
        "secti": lambda a, b: a + b,
        "odecti": lambda a, b: a - b,
        "nasob": lambda a, b: a * b,
        "vydel": lambda a, b: a / b,
        "mocnina": lambda a, b: a**b,
        "odmocnina": lambda a, b: a ** (1 / b),
    }.get(operace.lower(), None)

    odpoved = (
        f"Výsledek operace {operace} je {OPERACE(cislo1, cislo2)}"
        if OPERACE
        else "Operace není podporována"
    )

    return render_template("kalkulacka.html", odpoved=odpoved)


if __name__ == "__main__":
    app.run(debug=True)
