from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "123456789"

REGISTROVANI_UZIVATELE = {
    "admin": "admin",
    "kuba": "heslo123",
    "pepa": "hesl0"
}

@app.route("/")
def index():
    username = session.get("username")
    session["username"] = None
    return render_template("index.html", username=username)

@app.route("/validate", methods=["POST"])
def validate():
    username = request.form.get("username")
    password = request.form.get("password")

    usernames = REGISTROVANI_UZIVATELE.keys()
    if not username in usernames:
        session["chybova_hlaska"] = "Nesprávné jméno nebo heslo."
        return redirect(url_for("index"))
    if not REGISTROVANI_UZIVATELE[username] == password:
        session["chybova_hlaska"] = "Nesprávné jméno nebo heslo."
        return redirect(url_for("index"))
    session["username"] = username
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)