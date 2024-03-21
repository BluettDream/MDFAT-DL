from flask import Blueprint, request
from service import image_service
img = Blueprint('img', __name__)


@img.route("/image/matchPoints", methods=["POST"])
def process():
    tiny_img, big_img, threshold = request.files['tinyImg'], request.files['srcImg'], request.form['threshold']
    return image_service.match_template(tiny_img, big_img, threshold)
