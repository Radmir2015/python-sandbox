import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('data/wiki.jpg', 0)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()


plt.subplot(221)
plt.imshow(img, cmap='gray')

plt.subplot(222)
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
# plt.show()


cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

img2 = cdf[img]

hist, bins = np.histogram(img2.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.subplot(223)
plt.imshow(img2, cmap='gray')

plt.subplot(224)
plt.plot(cdf_normalized, color='b')
plt.hist(img2.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()



equ = cv.equalizeHist(img)
res = np.hstack((img, equ))

plt.imshow(res, cmap='gray')
plt.show()


tsukuba = cv.imread('data/tsukuba_l.jpg', 0)

# create a CLAHE object
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(tsukuba)

plt.imshow(np.hstack((tsukuba, cv.equalizeHist(tsukuba), cl1)), cmap='gray')
plt.show()
