from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

KOMENTARE = [
    {"name": "Petr", "comment": "Dobrý den, mám dotaz."},
    {"name": "Jana", "comment": "Super stránka!"},
    {"name": "Marie", "comment": "Děkuji za odpověď."},
    {"name": "Pavel", "comment": "Moc se mi líbí."},
]


@app.route("/")
def index():
    print(KOMENTARE)
    return render_template("index.html", komentare=KOMENTARE)


@app.route("/zpracuj-formular", methods=["POST"])
def zpracuj_formular():
    print(request.form)
    jmeno = request.form["name"]
    komentar = request.form.get("comment")
    print(jmeno, komentar)
    KOMENTARE.append({"name": jmeno, "comment": komentar})

    return redirect(url_for("index"))


@app.route("/zobraz-komentar/<int:index>")
def zobraz_komentar(index):
    if index >= len(KOMENTARE) or index < 0:
        return "Komentář neexistuje."
    komentar = KOMENTARE[index]
    return render_template("komentar.html", komentar=komentar)


if __name__ == "__main__":
    app.run(debug=True)
