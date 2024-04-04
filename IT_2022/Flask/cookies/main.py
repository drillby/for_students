from flask import Flask, request, make_response
import datetime

app = Flask(__name__)

@app.route("/set-cookie/<value>")
def set_cookie(value):
    res = make_response("nastavuju cookie")
    res.set_cookie("value", value, max_age=30)

    return res

@app.route("/get-cookie")
def get_cookie():
    cookie = request.cookies.get("value")

    return cookie

if __name__ == "__main__":
    app.run(debug=True)