from flask import Flask, render_template

app = Flask(__name__)


POLE = ["První", "Druhý", "Třetí", "Čtvrtý", "Pátý"]

SLOVNIK = [
    {"jmeno": "Jan", "prijmeni": "Novák", "vek": 30, "mesto": "Praha"},
    {"jmeno": "Petr", "prijmeni": "Svoboda", "vek": 25, "mesto": "Brno"},
    {"jmeno": "Jana", "prijmeni": "Dvořáková", "vek": 35, "mesto": "Ostrava"},
    {"jmeno": "Pavel", "prijmeni": "Kovář", "vek": 40, "mesto": "Plzeň"},
    {"jmeno": "Lucie", "prijmeni": "Nováková", "vek": 27, "mesto": "Liberec"},
]

SLOVNIK_2 = {"jmeno": "Jan", "prijmeni": "Novák", "vek": 30, "mesto": "Praha"}


@app.route("/")
def index():
    cislo = 10
    return render_template(
        "index.html", pole=POLE, slovnik=SLOVNIK, slovnik_2=SLOVNIK_2, cislo=cislo
    )


if __name__ == "__main__":
    app.run(debug=True)
