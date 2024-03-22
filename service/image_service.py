import cv2 as cv
import numpy as np
from werkzeug.datastructures import FileStorage
import matplotlib.pyplot as plt


def match_template(match_img: FileStorage, template_img: FileStorage, threshold: float) -> list:
    tiny_img = cv.imdecode(np.frombuffer(match_img.read(), np.uint8), cv.COLOR_BGR2GRAY)
    big_img = cv.imdecode(np.frombuffer(template_img.read(), np.uint8), cv.COLOR_BGR2GRAY)
    plt.imshow(big_img)
    plt.show()
    plt.imshow(tiny_img)
    plt.show()
    result = cv.matchTemplate(tiny_img, big_img, cv.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    points = []
    for pt in zip(*loc[::-1]):
        cv.rectangle(tiny_img, pt, (pt[0] + big_img.shape[1], pt[1] + big_img.shape[0]), (0, 0, 255), 2)
        cv.putText(tiny_img, 'Match', (pt[0], pt[1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        plt.imshow(tiny_img)
        plt.show()
        points.append(pt)
    return points
