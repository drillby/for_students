from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

KOMENTARE = [
    {
        "jmeno":"Pepa",
        "obsah":"Komentář 1",
    },
    {
        "jmeno":"Kuba",
        "obsah":"Komentář 2",
    },
    {
        "jmeno":"Petr",
        "obsah":"Komentář 3",
    },
]

@app.route("/")
def index():
    return render_template("index.html", komentare=KOMENTARE)

@app.route("/zpracuj-komentar", methods=["POST"])
def zpracuj_komenmtar():
    jmeno = request.form.get("jmeno")
    obsah = request.form.get("obsah")

    print(request.form)

    novy_komentar = {
        "jmeno": jmeno,
        "obsah": obsah
    }

    KOMENTARE.append(novy_komentar)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)