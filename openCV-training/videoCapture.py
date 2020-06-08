import numpy as numpy
import cv2 as cv

cap = cv.VideoCapture(0) # 'data/vtest.avi')

# define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi', fourcc, 24.0, (640, 480))

if not cap.isOpened():
    print('Cannot open camera')
    exit()

while True:
    # capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print('Can\'t receive frame (stream end?). Exiting...')
        break

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # display the resulting frame

    frame = cv.flip(frame, 0)

    out.write(frame)

    cv.imshow('frame', frame)

    if cv.waitKey(1000 // 24) == ord('q'):
        break

# when everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()