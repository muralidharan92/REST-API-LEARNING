"""Module providing flask modules, utils methods, Add, Sub, Mul, Div, Mod, Visit"""

from flask import Flask
from add import Add
from sub import Sub
from mul import Mul
from div import Div
from mod import Mod
from visit import Visit
from utils import get_users_visited_count

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_greeting_page():
    """This method will handle home api request"""
    return f"Hello Welcome to Learning session: {get_users_visited_count()}"


@app.route("/count", methods=["GET"])
def get_api_hit_count():
    """This method will handle count api request"""
    return Visit().get()


@app.route("/calc/2/add", methods=["POST"])
def calc_add():
    """This method will handle add api request"""
    return Add().post()


@app.route("/calc/2/sub", methods=["POST"])
def calc_sub():
    """This method will handle sub api request"""
    return Sub().post()


@app.route("/calc/2/mul", methods=["POST"])
def calc_mul():
    """This method will handle mul api request"""
    return Mul().post()


@app.route("/calc/2/div", methods=["POST"])
def calc_div():
    """This method will handle div api request"""
    return Div().post()


@app.route("/calc/2/mod", methods=["POST"])
def calc_mod():
    """This method will handle mod api request"""
    return Mod().post()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5080)
