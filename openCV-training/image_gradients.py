import numpy as np
import cv2 as cv

from extra_func import draw_images

img = cv.imread('data/sudoku.png', 0)

laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
scharrx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=-1)
sobelx_8u = np.uint8(np.absolute(sobelx))

draw_images([img, laplacian, sobelx, sobely, scharrx, sobelx_8u],
            ['original', 'laplacian', 'sobelx', 'sobely', 'scharrx', 'sobelx_8u'],
            cmap='gray')