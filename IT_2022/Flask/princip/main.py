# https://m3m4ndtv-5000.euw.devtunnels.ms/
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Jiný text"

@app.route("/strana2")
def dalsi_stranka():
    return "<h1 style='color:red'>Další stránka</h1>"

if __name__ == "__main__":
    app.run(debug=True)
