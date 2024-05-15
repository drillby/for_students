from flask import Flask, make_response, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "tajny_klic"


UZIVATELE = [
    {"username": "admin", "password": "admin"},
    {"username": "user", "password": "user"},
    {"username": "test", "password": "test"},
]


@app.route("/vytvor-cookie")
def vytvor_cookie():
    response = make_response("Cookie byla vytvořena.")
    response.set_cookie("barva", "red", max_age=20)
    return response


@app.route("/zobraz-cookie")
def zobraz_cookie():
    return render_template("index.html")


@app.route("/smaz-cookie")
def smaz_cookie():
    response = make_response("Cookie byla smazána.")
    response.set_cookie("barva", "", expires=0)
    return response


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("username")
    return "Odhlášení bylo úspěšné."


@app.route("/register", methods=["GET", "POST"])
def register():
    username = "admin"
    password = "heslo"

    for uzivatel in UZIVATELE:
        if uzivatel["username"] == username:
            return "Uživatel již existuje."

    uzivatel = {"username": username, "password": password}
    UZIVATELE.append(uzivatel)
    return str(UZIVATELE)


@app.route("/login", methods=["GET", "POST"])
def login():
    # Získání dat z formuláře
    username = "admin"
    password = "admin"

    for uzivatel in UZIVATELE:
        if uzivatel["username"] == username and uzivatel["password"] == password:
            session["username"] = username
            return "Přihlášení bylo úspěšné."

    return "Přihlášení bylo neúspěšné."


@app.route("/uloz-session/<string:data>")
def uloz_session(data):
    session["data"] = data
    return "Data byla uložena do session."


@app.route("/zobraz-session")
def zobraz_session():
    return session.get("data", "Data nebyla uložena do session.")


@app.route("/smaz-session")
def smaz_session():
    session.pop("data")
    return "Data byla smazána z session."


if __name__ == "__main__":
    app.run(debug=True)
