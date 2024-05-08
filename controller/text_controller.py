from flask import Blueprint, request
from service import text_service

txt = Blueprint('txt', __name__)


@txt.post("/text/matchPoints")
def process():
    img_list = request.json['imageLinkList']
    return text_service.extract_text(img_list)
