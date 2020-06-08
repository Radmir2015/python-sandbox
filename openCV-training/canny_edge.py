import numpy as np
import cv2 as cv


img = cv.imread('data/messi5.jpg', 0)
# edges = cv.Canny(img, 100, 200)


def draw_edges():
    edges = cv.Canny(img, cv.getTrackbarPos('minVal', 'canny'),
                     cv.getTrackbarPos('maxVal', 'canny'))
    cv.imshow('canny', edges)


def onChangeValue(x):
    draw_edges()


cv.namedWindow('canny')

cv.createTrackbar('minVal', 'canny', 0, 255, onChangeValue)
cv.createTrackbar('maxVal', 'canny', 0, 255, onChangeValue)

cv.setTrackbarPos('minVal', 'canny', 100)
cv.setTrackbarPos('maxVal', 'canny', 200)

cv.imshow('original', img)

while True:
    draw_edges()
    # edges = cv.Canny(img, cv.getTrackbarPos('minVal', 'canny'), cv.getTrackbarPos('maxVal', 'canny'))
    # cv.imshow('canny', edges)

    if cv.waitKey():
        break

cv.destroyAllWindows()


# from extra_func import draw_images

# draw_images([img, edges], ['img', 'edges'], cmap='gray')
