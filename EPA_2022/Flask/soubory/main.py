import json
import os

from flask import Flask

app = Flask(__name__)


def vypis_json(nazev_soubor):
    aktivni_soubor = os.path.dirname(__file__)  # soubory
    SITE_ROOT = os.path.realpath(aktivni_soubor)  # cestu ke složce "soubory"
    json_url = os.path.join(SITE_ROOT, "static/data", nazev_soubor)
    UZIVATELE = json.load(open(json_url, "r", encoding="utf-8"))

    return UZIVATELE


def uloz_do_json(nazev_souboru, data):

    aktivni_soubor = os.path.dirname(__file__)  # soubory
    SITE_ROOT = os.path.realpath(aktivni_soubor)  # cestu ke složce "soubory"
    json_url = os.path.join(SITE_ROOT, "static/data", nazev_souboru)
    with open(json_url, "w", encoding="utf-8") as soubor:
        json.dump(data, soubor, ensure_ascii=False, indent=2)


@app.route("/vypis-uzivatele/<string:jmeno>")
def vypis_uzivatele(jmeno):
    UZIVATELE = vypis_json("uzivatele.json")

    for uzivatel in UZIVATELE:
        if uzivatel["username"] == jmeno:
            # přihlášení
            # vrácení na index
            return uzivatel
    return "Uživatel neexistuje"


@app.route("/vytvor-uzivatele/<jmeno>/<heslo>")
def vytvor_uzivatele(jmeno, heslo):
    UZIVATELE = vypis_json("uzivatele.json")

    for uzivatel in UZIVATELE:
        if uzivatel["username"] == jmeno:
            return "Uživatel již existuje"

    novy_uzivatel = {"username": jmeno, "password": heslo}
    UZIVATELE.append(novy_uzivatel)

    uloz_do_json("uzivatele.json", UZIVATELE)

    return "Uživatel vytvořen"


@app.route("/smaz-uzivatele/<jmeno>")
def smaz_uzivatele(jmeno):
    UZIVATELE = vypis_json("uzivatele.json")

    for idx, uzivatel in enumerate(UZIVATELE):
        if uzivatel["username"] == jmeno:
            UZIVATELE.pop(idx)
            uloz_do_json("uzivatele.json", UZIVATELE)
            return "Uživatel smazán"
    return "Uživatel neexistuje"


@app.route("/zobraz-uzivatele/<string:jmeno>")
def zobraz_uzivatele(jmeno):
    UZIVATELE = vypis_json("uzivatele.json")

    for uzivatel in UZIVATELE:
        if uzivatel["username"] == jmeno:
            username = uzivatel["username"]
            barva = uzivatel["barva"]

            # normálně by se uložilo do cookies
            # následně by se barva četla z cookies v jiné cestě
            return f"<h1 style='color:{barva}'>{username}</h1>"
    return "Uživatel neexistuje"


if __name__ == "__main__":
    app.run(debug=True)
