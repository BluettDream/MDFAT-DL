import cv2 as cv
import numpy as np
from flask import jsonify, Response
from werkzeug.datastructures import FileStorage
from matplotlib import pyplot as plt


def match_template(match_img: FileStorage, template_img: FileStorage, threshold: float) -> Response:
    tiny_img = cv.imdecode(np.frombuffer(match_img.read(), np.uint8), cv.COLOR_RGB2GRAY)
    big_img = cv.imdecode(np.frombuffer(template_img.read(), np.uint8), cv.COLOR_RGB2GRAY)
    result = cv.matchTemplate(tiny_img, big_img, cv.TM_CCOEFF_NORMED)
    mn, ma, mn_loc, ma_loc = cv.minMaxLoc(result)
    cv.rectangle(big_img, ma_loc, (ma_loc[0] + tiny_img.shape[1], ma_loc[1] + tiny_img.shape[0]), 255, 2)
    # cv.imshow('Result', big_img)
    # cv.waitKey(0)
    return jsonify({
        'similarity': ma,
        'location': ma_loc
    })
