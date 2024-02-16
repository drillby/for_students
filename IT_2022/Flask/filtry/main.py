from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<text>/<int:posun>")
def index(text, posun):
    return render_template("index.html", text=text, posun=posun)


@app.template_filter("muj_filtr")
def velka_pismena(text):
    return text.upper()

@app.template_filter("zopakuj")
def velka_pismena(text, pocet_opakovani):
    return pocet_opakovani*text

@app.template_filter("caesar")
def caesar_cipher(text: str, shift: int):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
            # raise  ValueError("Znak ", char, " není písmeno!")
    return encrypted_text



if __name__ == "__main__":
    app.run(debug=True)