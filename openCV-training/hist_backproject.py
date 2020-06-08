import numpy as np
import cv2 as cv

roi = cv.imread('data/messi_ground.png')
hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

target = cv.imread('data/messi5.jpg')
target = cv.resize(target, None, fx=0.7, fy=0.7)
hsvt = cv.cvtColor(target, cv.COLOR_BGR2HSV)

roihist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

cv.normalize(roihist, roihist, 0, 255, cv.NORM_MINMAX)
dst = cv.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
cv.filter2D(dst, -1, disc, dst)

ret, thresh = cv.threshold(dst, 50, 255, 0)
thresh = cv.merge((thresh, thresh, thresh))
res = cv.bitwise_and(target, thresh)

res = np.hstack((target, thresh, res))
cv.imshow('result', res)

cv.waitKey()
cv.destroyAllWindows()