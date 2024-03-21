import cv2 as cv
import numpy as np


def match_template(tiny_img, big_img, threshold):
    tiny_img = cv.imdecode(np.fromstring(tiny_img, np.uint8), cv.IMREAD_UNCHANGED)
    big_img = cv.imdecode(np.fromstring(big_img, np.uint8), cv.IMREAD_UNCHANGED)
    img_gray = cv.cvtColor(tiny_img, cv.COLOR_BGR2GRAY)
    template = cv.cvtColor(big_img, cv.COLOR_BGR2GRAY)
    result = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    points = []
    for pt in zip(*loc[::-1]):
        points.append(pt)
    return points
