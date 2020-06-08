import numpy as np
import cv2 as cv

yellow_hsv = [ 26, 230, 255]

cap = cv.VideoCapture('data/vtest.avi')

while True:
    ret, frame = cap.read()

    if not ret:
        print('Stream ended.')
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_yellow = np.array([26 - 5, 100, 100])
    upper_yellow = np.array([26 + 5, 255, 255])

    mask = cv.inRange(hsv, lower_yellow, upper_yellow)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    if cv.waitKey(1000 // 24) == ord('q'):
        break

cap.release()

cv.destroyAllWindows()