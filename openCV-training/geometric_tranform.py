import numpy as np
import cv2 as cv

img = cv.imread('data/messi5.jpg', 1)
sudoku_img = cv.imread('data/sudoku.png')
# drawing_img = cv.imread('data/drawing.png')

res = cv.resize(img, None, fx=1/1.5, fy=1/1.5, interpolation=cv.INTER_CUBIC)

# print(img.shape, img.shape[:2]) # (342, 548, 3) (342, 548)

height, width = res.shape[:2]
# res = cv.resize(img, (width * 2, height * 2), interpolation=cv.INTER_CUBIC)

points1 = np.float32([[50, 50], [200, 50], [50, 200]])
points2 = np.float32([[10, 100], [200, 50], [100, 250]])

sudoku_pts1 = np.float32([[74, 82], [487, 70], [32, 510], [519, 515]])
sudoku_pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = np.float32([[1, 0, 100], [0, 1, 50]])
M_rot = cv.getRotationMatrix2D(
    ((width - 1) / 2.0, (height - 1) / 2.0), 90, 0.7)
M_affine = cv.getAffineTransform(points1, points2)
M_persp = cv.getPerspectiveTransform(sudoku_pts1, sudoku_pts2)

warp_a = cv.warpAffine(res, M, (width, height))
rot = cv.warpAffine(res, M_rot, (width, height))
aff = cv.warpAffine(res, M_affine, (res.shape[:2]))
sudoku = cv.warpPerspective(sudoku_img, M_persp, (300, 300))

cv.imshow('res', res)
cv.imshow('warp_a', warp_a)
cv.imshow('rot', rot)

from matplotlib import pyplot as plt

print(img.shape, aff.shape)

# plt.subplot(121), plt.imshow(res[:, :, ::-1]), plt.title('Input')
# plt.subplot(122), plt.imshow(aff[:, :, ::-1]), plt.title('Output')
# plt.show()

plt.subplot(121), plt.imshow(sudoku_img), plt.title('Input')
plt.subplot(122), plt.imshow(sudoku), plt.title('Output')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
