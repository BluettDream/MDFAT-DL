from flask import Blueprint, request
from service import image_service
img = Blueprint('img', __name__)


@img.route("/image/matchPoints", methods=["POST"])
def process():
    tiny_img, big_img = request.files['matchImage.png'], request.files['templateImage.png']
    return image_service.match_template(tiny_img, big_img)
