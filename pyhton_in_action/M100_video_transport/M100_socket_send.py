import socket
import time
import cv2
import time
import thread
import numpy as np

# socket init
# send video to 9992
addr_to = ('127.0.0.1',9992)
# receive cmd from 8881
addr_from = ('127.0.0.1',8881)
# send video socket,and recieve cmd
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addr_from)
# # receive cmd socket
# s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s1.bind(addr_from)

# camera0~2
cap0 = cv2.VideoCapture(3)
cap1 = cv2.VideoCapture(5)
cap2 = cv2.VideoCapture(7)
# setting camera0's picture size
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap0.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
# setting camera1's picture size
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
# setting camera2's picture size
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
# read camera data
ret,frame0 = cap0.read()
ret,frame1 = cap1.read()
ret,frame2 = cap2.read()
# save
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out0 = cv2.VideoWriter('/home/wsn/Documents/python/pyhton_in_action/store/output0.avi'\
,fourcc,30,(1280,720))
out1 = cv2.VideoWriter('/home/wsn/Documents/python/pyhton_in_action/store/output1.avi'\
,fourcc,30,(1280,720))
out2 = cv2.VideoWriter('/home/wsn/Documents/python/pyhton_in_action/store/output2.avi'\
,fourcc,30,(1280,720))

# data = ['']
send_video0 = [False]
send_video1 = [False]
send_video2 = [False]

def data_thread(threadname,num):
    while True:
        data,addr_1 = s.recvfrom(60000)
        print "receive data: ", data,"from",addr_1
        if data == '4':
            send_video0[0] = True
            send_video1[0] = False
            send_video2[0] = False
            # print "send_video0=",send_video0[0],"send_video1=",send_video1[0],"send_video2=",send_video2[0]
        elif data == '6':
            send_video0[0] = False
            send_video1[0] = True
            send_video2[0] = False
            # print "send_video0=",send_video0[0],"send_video1=",send_video1[0],"send_video2=",send_video2[0]
        elif data == '8':
            send_video0[0] = False
            send_video1[0] = False
            send_video2[0] = True
            # print "send_video0=",send_video0[0],"send_video1=",send_video1[0],"send_video2=",send_video2[0]
        else:
            send_video0[0] = False
            send_video1[0] = False
            send_video2[0] = False

thread.start_new_thread(data_thread,("data_thread",1))

while True:

    if send_video0[0] and not send_video1[0] and not send_video2[0]:
        # cv2.imshow('show',frame0)
        # key = cv2.waitKey(1)

        # encode frame0 into jpeg
        ret,buff = cv2.imencode('.jpg',frame0,[int(cv2.IMWRITE_JPEG_QUALITY),75])
        # change the buff into array
        data = np.array(buff)
        # convert data to string
        stringdata = data.tostring()
        # print len(stringdata)

        # sending data to client
        count = 0
        max_size = 60000
        while count < len(stringdata):
            if count + max_size > len(stringdata):
                s.sendto(stringdata[count:],addr_to)
            else:
                s.sendto(stringdata[count:count+max_size],addr_to)
            count += max_size
        # print "send one camera0 frame"

    elif send_video1[0] and not send_video0[0] and not send_video2[0]:
        # cv2.imshow('show',frame1)
        # key = cv2.waitKey(1)

        # encode frame1 into jpeg
        ret,buff = cv2.imencode('.jpg',frame1,[int(cv2.IMWRITE_JPEG_QUALITY),75])
        # convert buff to array
        data = np.array(buff)
        # conver array to string
        stringdata = data.tostring()
        # print len(stringdata)

        # sending data to client
        count = 0
        max_size = 60000
        while count < len(stringdata):
            if count + max_size > len(stringdata):
                s.sendto(stringdata[count:],addr_to)
            else:
                s.sendto(stringdata[count:count+max_size],addr_to)
            count += max_size
        # print "send one camera1 frame"
    elif send_video2[0] and not send_video0[0] and not send_video1[0]:
        # cv2.imshow('show',frame1)
        # key = cv2.waitKey(1)

        # encode frame1 into jpeg
        ret,buff = cv2.imencode('.jpg',frame2,[int(cv2.IMWRITE_JPEG_QUALITY),75])
        # convert buff to array
        data = np.array(buff)
        # conver array to string
        stringdata = data.tostring()
        # print len(stringdata)

        # sending data to client
        count = 0
        max_size = 60000
        while count < len(stringdata):
            if count + max_size > len(stringdata):
                s.sendto(stringdata[count:],addr_to)
            else:
                s.sendto(stringdata[count:count+max_size],addr_to)
            count += max_size
        # print "send one camera1 frame"
    else:
        pass


    ret,frame0 = cap0.read()
    ret,frame1 = cap1.read()
    ret,frame2 = cap2.read()

    # dt = datetime.datetime.now()
    # cv2.putText(frame0,str(dt),(10,frame0.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX\
    # ,1.35,(0,0,255),1)
    # cv2.putText(frame1,str(dt),(10,frame1.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX\
    # ,1.35,(0,0,255),1)
    out0.write(frame0)
    out1.write(frame1)
    out2.write(frame2)


s.close()
cap0.release()
cap1.release()
cap2.release()
