import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('data/home.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

plt.hist(img_gray.ravel(), 256, [0, 255])
plt.show()

for i, col in enumerate(['b', 'g', 'r']):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.show()

# mask creation
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img_gray, img_gray, mask=mask)

# histogram with and without mask
hist_full = cv.calcHist([img_gray], [0], None, [256], [0, 255])
hist_mask = cv.calcHist([img_gray], [0], mask, [256], [0, 256])

plt.subplot(221), plt.imshow(img_gray, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])

plt.show()