import numpy as np
import cv2 as cv

img = cv.imread('data/star1.jpg', 0)
# img = cv.resize(img, None, fx=1/1.5, fy=1/1.5)
ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# thresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 21, 11)

contours, heirarchy = cv.findContours(thresh, 1, 2)

img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

cv.drawContours(img, contours, 0, (127, 255, 0), 5)

cnt = contours[0]
M = cv.moments(cnt)
print(M)

cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])

print('Centroid: ({}, {})'.format(cx, cy))
cv.circle(img, (cx, cy), 10, (255, 255, 255), -1)

print('Area:', cv.contourArea(cnt))
print('Perimeter:', cv.arcLength(cnt, True))

epsilon = 0.02 * cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)
# approx = approx.reshape((-1, 1, 2))

# cv.polylines(img, approx, True, (123, 32, 200), 5)
cv.drawContours(img, [approx], 0, (232, 11, 0), 3)
# print('Apporx:', approx)

hull = cv.convexHull(cnt)
# cv.polylines(img, hull, True, (32, 132, 100), 7)
cv.drawContours(img, [hull], 0, (103, 234, 240), 2)
# print('Hull:', hull)

k = cv.isContourConvex(cnt)
print('ContourConvex:', k)

cv.imshow('img', img)
cv.waitKey()

img = cv.imread('data/lightning.jpg', 0)
ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
contours, heirarchy = cv.findContours(thresh, 1, 2)
cnt = contours[1]





# properties

x, y, w, h = cv.boundingRect(cnt)
aspect_ratio = float(w) / h
print('Aspect ratio:', aspect_ratio)

area = cv.contourArea(cnt)
x, y, w, h = cv.boundingRect(cnt)
rect_area = w * h
extent = float(area) / rect_area
print('Extent:', extent)

area = cv.contourArea(cnt)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area) / hull_area
print('Solidity:', solidity)

area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4 * area / np.pi)
print('Equivalent Diameter:', equi_diameter)

(x, y), (MA, ma), angle = cv.fitEllipse(cnt)
print('Orientation (x, y, Ma, ma, angle):', x, y, MA, ma, angle)

mask = np.zeros(img.shape, np.uint8)
# cv.drawContours(mask, [cnt], 0, 255, -1)
# pixelpoints = np.transpose(np.nonzero(mask))
pixelpoints = cv.findNonZero(mask)
print('pixelpoints:', pixelpoints)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(img, mask=mask)
print('min_val, max_val, min_loc, max_loc =', min_val, max_val, min_loc, max_loc)

mean_val = cv.mean(img, mask=mask)
print('Mean:', mean_val)

leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
print('Leftmost, rightmost, topmost, bottommost =', leftmost, rightmost, topmost, bottommost)



img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

cv.drawContours(img, contours, -1, (234, 12, 35), 2)

x, y, w, h = cv.boundingRect(cnt)
cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

rect = cv.minAreaRect(cnt)
box = np.int0(cv.boxPoints(rect))
cv.drawContours(img, [box], 0, (0, 0, 255), 2)

(x, y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
cv.circle(img, center, radius, (255, 0, 0), 2)

ellipse = cv.fitEllipse(cnt)
cv.ellipse(img, ellipse, (127, 127, 0), 2)

row, cols = img.shape[:2]
[vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv.line(img, (cols - 1, righty), (0, lefty), (0, 127, 127), 2)



cv.imshow('img', img)

cv.waitKey()
cv.destroyAllWindows()