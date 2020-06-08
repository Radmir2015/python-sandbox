import numpy as np
import cv2 as cv

img1 = cv.imread('data/ml.png')
img2 = cv.imread('data/opencv-logo.png')

print(img1.shape, img2.shape)

img1_resized = cv.resize(img1, (img2.shape[1], img2.shape[0]))

dst = cv.addWeighted(img1_resized, 0.7, img2, 0.3, 0)

cv.namedWindow('dst', cv.WINDOW_NORMAL)
cv.imshow('dst', dst)
cv.waitKey(0)

# Load two images
img1 = cv.imread('data/messi5.jpg')
img2 = cv.imread('data/opencv-logo-white.png')

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('mask', mask)
cv.waitKey(0)
cv.imshow('mask_inv', mask_inv)
cv.waitKey(0)

cv.imshow('img1_bg', img1_bg)
cv.waitKey(0)
cv.imshow('img2_fg', img2_fg)
cv.waitKey(0)


cv.imshow('res', img1)
cv.waitKey(0)


cv.destroyAllWindows()
