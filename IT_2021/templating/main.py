from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


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


@app.route("/produkt/<string:nazev>/<int:cena>")
def render_produkt(nazev, cena):
    return render_template("produkt.html", produkt=nazev, cena=cena)


if __name__ == "__main__":
    app.run(debug=True)
