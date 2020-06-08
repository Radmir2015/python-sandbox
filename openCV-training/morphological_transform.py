import numpy as np
import cv2 as cv
import math
import random

from matplotlib import pyplot as plt


def sp_noise(image, prob, color=255):
    output = np.zeros(image.shape, np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = color  # random.sample([0, 255], 1)
            else:
                output[i][j] = image[i][j]
    return output


img = cv.imread('data/j.png', 1)
# img = cv.resize(img, None, fx=2, fy=2)
noisy_white = sp_noise(img, 0.7)
noisy_black = sp_noise(img, 0.7, color=0)

kernel = np.ones((5, 5), np.uint8)
kern9 = np.ones((9, 9), np.uint8)

# cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
# cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))

erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)
opening = cv.morphologyEx(noisy_white, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(noisy_black, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kern9)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kern9)

titles = ['original', 'erosion', 'dilation',
          'noisy_white', 'opening', 'noisy_black', 'closing', 'gradient', 'tophat', 'blackhat']
images = [img, erosion, dilation, noisy_white, opening,
          noisy_black, closing, gradient, tophat, blackhat]

# print(math.ceil(len(img) / 3), math.ceil(len(img) / math.ceil(len(img) / 3)))

import extra_func

extra_func.draw_images(images, titles, (2, 1))

# for im, t, inx in zip(images, titles, range(len(images))):
#     plt.subplot(math.ceil(len(images) / 3),
#                 math.ceil(len(images) / math.ceil(len(images) / 3)), inx + 1)
#     plt.imshow(im)
#     plt.title(t)
#     plt.xticks([]), plt.yticks([])

# plt.show()
