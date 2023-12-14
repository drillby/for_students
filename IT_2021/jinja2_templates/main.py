from dataclasses import dataclass

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.template_filter("muj_filtr")
def muj_filtr(text):
    text = list(text)
    for idx in range(0, len(text), 2):
        text[idx] = text[idx].upper()

    text = "".join(text)

    return text


@app.route("/")
def index():
    return """
    <h1>Flask Template</h1>4
    <p>Flask is fun!</p>
    <ul>
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ul>
    """


@app.route("/render_template")
def template_render():
    return render_template("index.html")


@app.route("/produkt/<int:id>")
def render_produkt(id):
    produkty = {
        1: ("Ford Focus 2005", 55_000),
        2: ("BMW E46", 150_000),
        3: ("Fiat Multipla", 500_000),
    }

    @dataclass
    class Produkt:
        nazev: str
        cena: str

    p1 = Produkt("Fiat Multipla", 500_000)

    if id not in produkty.keys():
        return "<h1>Produkt neexistuje</h1>"
    produkt = produkty[id]
    return render_template("produkt.html", nazev=produkt[0], cena=produkt[1], objekt=p1)


@app.route("/forcyklus")
def forcyklus():
    oblibena_jidla = ["Svíčková", "Guláš", "Ramen", "Gdousihogulas"]
    return render_template("ukazka_cyklu.html", oblibena_jidla=oblibena_jidla)


@app.route("/podminka/<uzivatel>")
def podminky(uzivatel):
    uzivatele = ("pepa", "pavel", "kuba")
    uzivatel = "Tohle je hrozne dlouhy text"
    return render_template("ukazka_podminky.html", uzivatele=uzivatele, vstup=uzivatel)


if __name__ == "__main__":
    app.run(debug=True)
