import numpy as np
import cv2 as cv
import random

from matplotlib import pyplot as plt


def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape, np.uint8)
    # thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            # elif rdn > thres:
            #     output[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            else:
                output[i][j] = image[i][j]
    return output


img = cv.imread('data/opencv-logo-white.png')
rubber_whale = cv.imread('data/rubberwhale1.png')

kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)

blur = cv.blur(img, (5, 5))
blur_1 = cv.GaussianBlur(img, (5, 5), 0)

salt_pepper_noise = sp_noise(img, 0.3)
median = cv.medianBlur(salt_pepper_noise, 5)

bilateral = cv.bilateralFilter(rubber_whale, 9, 75, 75)


plt.subplot(241), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(242), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.subplot(243), plt.imshow(blur), plt.title('Blur')
plt.xticks([]), plt.yticks([])

plt.subplot(244), plt.imshow(blur_1), plt.title('Blur (Gaussian)')
plt.xticks([]), plt.yticks([])

plt.subplot(245), plt.imshow(salt_pepper_noise), plt.title('Salty')
plt.xticks([]), plt.yticks([])

plt.subplot(246), plt.imshow(median), plt.title('Median')
plt.xticks([]), plt.yticks([])

plt.subplot(247), plt.imshow(rubber_whale), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(248), plt.imshow(bilateral), plt.title('Bilaterial')
plt.xticks([]), plt.yticks([])

plt.show()
