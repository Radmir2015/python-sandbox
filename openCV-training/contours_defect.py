import cv2 as cv
import numpy as np

img = cv.imread('data/star1.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]

dist = cv.pointPolygonTest(cnt, (100, 250), True)
print('Distance:', dist)

hull = cv.convexHull(cnt, returnPoints=False)
defects = cv.convexityDefects(cnt, hull)

cv.circle(img, (100, 250), 5, [255, 255, 0], -1)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])

    cv.line(img, start, end, [0, 255, 0], 2)
    cv.circle(img, far, 5, [0, 0, 255], -1)

cv.imshow('img', img)
cv.waitKey(0)


img1 = cv.imread('data/star1.jpg', 0)
img2 = cv.imread('data/lightning.jpg', 0)

ret, thresh1 = cv.threshold(img1, 127, 255, 0)
ret, thresh2 = cv.threshold(img2, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh1, 2, 1)
cnt1 = contours[0]
contours, hierarchy = cv.findContours(thresh2, 2, 1)
cnt2 = contours[1]

ret = cv.matchShapes(cnt1, cnt2, 1, 0.0)
print('Match shapes:', ret)



cv.destroyAllWindows()