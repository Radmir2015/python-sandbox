import numpy as np
import cv2 as cv

A = cv.imread('data/apple.jpg')
B = cv.imread('data/orange.jpg')

G = A.copy()
gpA = [G]

for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)

G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i - 1], GE)
    lpA.append(L)

lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i - 1], GE)
    lpB.append(L)

LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape

    ls = np.hstack((la[:, :cols//2], lb[:, cols//2:]))
    LS.append(ls)

ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])

real = np.hstack((A[:, :cols//2], B[:, cols//2:]))

from extra_func import draw_images

draw_images([ls_[:, :, ::-1], real[:, :, ::-1]], ['pyramid blending', 'direct blending'])