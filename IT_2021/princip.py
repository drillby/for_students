from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def root():
    a = "42"
    b = int(a)
    return "<h1>Ahoj světe další text!</h1>"

@app.route("/jmeno/<jmeno>")
def vypis_jmeno(jmeno):
    return f"<h1>Ahoj {escape(jmeno)}</h1>"

if __name__ == "__main__":
    app.run(debug=True)