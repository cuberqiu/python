import cv2

# camera0
cap0 = cv2.VideoCapture(1)

# setting camera0's picture size
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap0.set(cv2.CAP_PROP_FRAME_WIDTH,1280)

ret,frame0 = cap0.read()

while True:
    cv2.imshow('show',frame0)
    key = cv2.waitKey(1)

    ret,frame0 = cap0.read()

cap0.release()
