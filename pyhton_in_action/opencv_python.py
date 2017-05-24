import cv2

capture0 = cv2.VideoCapture(0)
capture1 = cv2.VideoCapture(1)


#img = cv2.imread('/home/wsn/Pictures/screenshot.png')

#cv2.namedWindow('Video',cv2.WND_PROP_FULLSCREEN)
cv2.namedWindow('Video')
cv2.setWindowProperty('Video',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

#cv2.imshow('Video',img)
#cv2.waitKey(0)

_, frame0 = capture0.read()
_, frame1 = capture1.read()
show_0 = True

while frame0 is not None or frame1 is not None:
    if show_0:
        cv2.imshow('Video',frame0)
        key = cv2.waitKey(10)
    else:
        cv2.imshow('Video',frame1)
        key = cv2.waitKey(10)

    if  key == ord('1'):
        show_0 = False
    elif key == ord('2'):
        show_0 =True
    elif key == ord('q'):
        break
    _, frame0 = capture0.read()
    _, frame1 = capture1.read()

cv2.destroyWindow('Video')
