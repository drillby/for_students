from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<string:text>")
def index(text):
    return render_template("index.html", jmeno=text)

@app.route("/<jmeno>/<prijmeni>")
def routing(jmeno, prijmeni):
    return jmeno + " " + prijmeni

@app.route("/<int:cislo>")
def routing_dt(cislo):
    return str(3*cislo)


if __name__ == "__main__":
    app.run(debug=True)