from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<int:cislo>/<int:cislo_2>")
def index(cislo, cislo_2):
    promenna = ["Špagety", "Svíčková", "Knedlo vepřo zelo"]
    slovnik = {
        "klic1":1,
        "klic2":3.14,
        "klic3":"text"
    }
    return render_template("index.html", promenna=promenna, slovnik=slovnik, cislo=cislo, cislo_2=cislo_2)

if __name__ == "__main__":
    app.run(debug=True)