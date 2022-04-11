import os
import flask
import random

app = flask.Flask(__name__)


def getPlanet():
    planets = [
        "Mercury",
        "Venus",
        "Mars",
        "Saturn",
        "Jupiter",
        "Neptune",
        "Uranus",
        "Pluto",
    ]
    planet = planets[random.randint(0, 7)]
    return planet


@app.route("/Mercury")
def Mercury():
    return flask.render_template("Mercury.html")


@app.route("/Pluto")
def Pluto():
    return flask.render_template("Pluto.html")


@app.route("/Venus")
def Venus():
    return flask.render_template("Venus.html")


@app.route("/Mars")
def Mars():
    return flask.render_template("Mars.html")


@app.route("/Saturn")
def Saturn():
    return flask.render_template("Saturn.html")


@app.route("/Jupiter")
def Jupiter():
    return flask.render_template("Jupiter.html")


@app.route("/Neptune")
def Neptune():
    return flask.render_template("Neptune.html")


@app.route("/Uranus")
def Uranus():
    return flask.render_template("Uranus.html")


@app.route("/Sources", methods=["GET", "POST"])
def sources():
    return flask.render_template("sources.html")


@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        return flask.redirect(f"/{getPlanet()}")

    return flask.render_template("index.html")


app.run(
    host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080")), debug=True
)
