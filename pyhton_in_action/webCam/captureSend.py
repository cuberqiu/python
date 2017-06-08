import numpy as np
import cv2
from socket import *
import time

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap0.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH,1280)


s = socket(AF_INET,SOCK_DGRAM)
host = '192.168.0.109'
# host = '127.0.0.1'
port = 9996
addr = (host,port)

# cv2.namedWindow('show',cv2.WND_PROP_FULLSCREEN)
ret,frame0 = cap0.read()
ret,frame1 = cap1.read()

show_0 = True
key = '0'

while True:

    if show_0:
        cv2.imshow('show',frame0)
        key = cv2.waitKey(1)

        ret,buff = cv2.imencode('.jpg',frame0,[int(cv2.IMWRITE_JPEG_QUALITY),75])
        data = np.array(buff)
        stringdata = data.tostring()
        print len(stringdata)
    else:
        cv2.imshow('show',frame1)
        key = cv2.waitKey(1)

        ret,buff = cv2.imencode('.jpg',frame1,[int(cv2.IMWRITE_JPEG_QUALITY),75])
        data = np.array(buff)
        stringdata = data.tostring()
        print len(stringdata)

    if key == ord('1'):
        show_0 = False
    elif key == ord('0'):
        show_0 = True


    count = 0
    while count < len(stringdata):
        if count + 60000 > len(stringdata):
            s.sendto(stringdata[count:],addr)
        else:
            s.sendto(stringdata[count:count+60000],addr)
        count += 60000
    print "send one frame"

    ret,frame0 = cap0.read()
    ret,frame1 = cap1.read()

cap.release()
