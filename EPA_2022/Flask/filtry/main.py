from flask import Flask, render_template

app = Flask(__name__)




@app.template_filter("zopakuj")
def zopakuj(text, pocet=3):
    return text * pocet


@app.template_filter("caesar")
def caesar(text: str, posun=3):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    vysledek = ""
    for pismeno in text:
        if pismeno.isalpha():
            if pismeno.islower():
                vysledek += abeceda[(abeceda.index(pismeno) + posun) % 26]
            else:
                vysledek += abeceda[
                    (abeceda.index(pismeno.lower()) + posun) % 26
                ].upper()
        else:
            vysledek += pismeno
    return vysledek

@app.route("/<string:text>/<int:pocet>")
def index(text, pocet):
    return render_template("index.html", text=text, pocet=pocet)

if __name__ == "__main__":
    app.run(debug=True)
