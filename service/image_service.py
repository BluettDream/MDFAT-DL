import cv2 as cv
import numpy as np
from flask import jsonify, Response
from werkzeug.datastructures import FileStorage


def match_template(match_img: FileStorage, template_img: FileStorage, threshold: float) -> Response:
    tiny_img = cv.imdecode(np.frombuffer(match_img.read(), np.uint8), cv.COLOR_BGR2GRAY)
    big_img = cv.imdecode(np.frombuffer(template_img.read(), np.uint8), cv.COLOR_BGR2GRAY)
    result = cv.matchTemplate(tiny_img, big_img, cv.TM_CCOEFF_NORMED)
    mn, ma, mn_loc, ma_loc = cv.minMaxLoc(result)
    return jsonify(list(ma_loc))
