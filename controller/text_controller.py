from flask import Blueprint

txt = Blueprint('txt', __name__)


@txt.route("/text/")
def process():
    return "Text processing..."
