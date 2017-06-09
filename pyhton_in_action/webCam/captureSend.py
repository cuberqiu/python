'''
    Web Camera Transporting
    Author:Cuber Qiu
    2017-06-09

    This is Server:
    Using pyhton capture usb camera data , and decoding it into jpeg and splict
    it into small fragmentations, then send them to client
    I add a function:
    we can collect data from two camera switching by clicking 1 or 0.
'''

import numpy as np
import cv2
from socket import *
import datetime

# camera0
cap0 = cv2.VideoCapture(1)
# camera1
cap1 = cv2.VideoCapture(3)

# setting camera0's picture size
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap0.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
# setting camera1's picture size
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH,1280)

# UDP initialization
s = socket(AF_INET,SOCK_DGRAM)
# destination ip
host = '192.168.0.112'
# destination port
port = 9996
# address must be setted as a tuple
addr = (host,port)

# save
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out0 = cv2.VideoWriter('/home/wsn/Documents/python/pyhton_in_action/webCam/output0.avi'\
,fourcc,30,(1280,720))
out1 = cv2.VideoWriter('/home/wsn/Documents/python/pyhton_in_action/webCam/output1.avi'\
,fourcc,30,(1280,720))

ts_file0 = open('/home/wsn/Documents/python/pyhton_in_action/webCam/ts_file0.txt','w+r')
ts_file1 = open('/home/wsn/Documents/python/pyhton_in_action/webCam/ts_file1.txt','w+r')

# cv2.namedWindow('show',cv2.WND_PROP_FULLSCREEN)
# read camera data
ret,frame0 = cap0.read()
ret,frame1 = cap1.read()

# if show_0 == True ,send camera0's data
# if show_0 == False ,send camera1's data
show_0 = True
# which keyboard u clicked, initialized with '0'
key = '0'

while True:
    if show_0:
        cv2.imshow('show',frame0)
        key = cv2.waitKey(1)

        # encode frame0 into jpeg
        ret,buff = cv2.imencode('.jpg',frame0,[int(cv2.IMWRITE_JPEG_QUALITY),75])
        # change the buff into array
        data = np.array(buff)
        # convert data to string
        stringdata = data.tostring()
        print len(stringdata)
    else:
        cv2.imshow('show',frame1)
        key = cv2.waitKey(1)

        # encode frame1 into jpeg
        ret,buff = cv2.imencode('.jpg',frame1,[int(cv2.IMWRITE_JPEG_QUALITY),75])
        # convert buff to array
        data = np.array(buff)
        # conver array to string
        stringdata = data.tostring()
        print len(stringdata)

    if key == ord('1'):
        show_0 = False
    elif key == ord('0'):
        show_0 = True

    # sending data to client
    count = 0
    max_size = 60000
    while count < len(stringdata):
        if count + max_size > len(stringdata):
            s.sendto(stringdata[count:],addr)
        else:
            s.sendto(stringdata[count:count+max_size],addr)
        count += max_size
    print "send one frame"

    ret,frame0 = cap0.read()
    ret,frame1 = cap1.read()

    # dt = datetime.datetime.now()
    # cv2.putText(frame0,str(dt),(10,frame0.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX\
    # ,1.35,(0,0,255),1)
    # cv2.putText(frame1,str(dt),(10,frame1.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX\
    # ,1.35,(0,0,255),1)
    dt = datetime.datetime.now()
    ts_file0.write(str(dt)+'\n')
    out0.write(frame0)

    dt = datetime.datetime.now()
    ts_file1.write(str(dt)+'\n')
    out1.write(frame1)

cap.release()
s.close()
