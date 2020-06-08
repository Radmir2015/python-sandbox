import numpy as np
import cv2 as cv

# Load a color image in grayscale
img = cv.imread('data/messi5.jpg', cv.IMREAD_COLOR)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)

k = cv.waitKey(0)

if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('messigray.png', img)
    cv.destroyAllWindows()



from matplotlib import pyplot as plt

plt.imshow(img[:, :, ::-1], cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

# cv.cvtColor(img, cv.COLOR_BGR2RGB)