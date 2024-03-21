from flask import Blueprint

img = Blueprint('img', __name__)


@img.route("/image/")
def process():
    return "Image processing..."
