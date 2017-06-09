import numpy as np
import cv2
import socket

img_to_read = b''
img_to_show = b''

addr = ('127.0.0.1',9996)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addr)

# cv2.namedWindow('cam')

max_size = 60000
while True:
    stringdata,address = s.recvfrom(max_size)
    while True:
        # the last splice
        if len(stringdata) == 0:
            if img_to_read != '':
                img_to_show = img_to_read
                img_to_read = ''
            print "receive one frame"
            break
        # the last splice
        if (len(stringdata)<max_size) and (len(stringdata)>0):
            img_to_read += stringdata
            img_to_show = img_to_read
            img_to_read = ''
            print "receive one frame"
            print 'len = %r' %len(img_to_show)
            break
        img_to_read += stringdata
        stringdata,address = s.recvfrom(max_size)

    # print len(img_to_show)
    # print img_to_show
    data_show = np.fromstring(img_to_show,dtype=np.uint8)
    print data_show
    print data_show[0]
    print data_show[(len(data_show)-2):]
    if data_show[0]==0xff and data_show[1]==0xd8 and \
    data_show[len(data_show)-2]==0xff and data_show[len(data_show)-1]==0xd9:
        # print len(data_show)
        img_decoded = cv2.imdecode(data_show,1)
        # print img_decoded

        if img_decoded == None:
            print "img is empty"
        else:
            cv2.imshow('cam',img_decoded)
            cv2.waitKey(1)
