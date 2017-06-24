# coding:utf-8
import socket
import numpy as np
import cv2
import thread
import time

# socket initialization
# receive cmd
addr1_from = ('127.0.0.1',9991)
# receive video
addr2_from = ('127.0.0.1',9992)

# send cmd to 8881
addr1_to = ('127.0.0.1',8881)


# receive cmd from m100, and send cmd to client
s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s1.bind(addr1_from)
# receive video data from s2
s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s2.bind(addr2_from)


# save
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out0 = cv2.VideoWriter('/home/wsn/Documents/python/pyhton_in_action/store/output_local0.avi'\
,fourcc,30,(1280,720))
out1 = cv2.VideoWriter('/home/wsn/Documents/python/pyhton_in_action/store/output_local1.avi'\
,fourcc,30,(1280,720))

# 自动尺寸显示
cv2.namedWindow('show',cv2.WND_PROP_AUTOSIZE)

# 全屏显示
# cv2.namedWindow('Video',cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty('Video',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

# camera
cap0 = cv2.VideoCapture(0)
ret,frame0 = cap0.read()
cap1 = cv2.VideoCapture(1)
ret,frame1 = cap0.read()

max_size = 60000

show_local = [True]
show_local_camera0 = [True]
recieve_video = [False]

img_to_read = b''
img_to_show = b''

# data thread
def data_thread(threadname,num):
        while True:
            data,addr_1 = s1.recvfrom(max_size)
            print "receive data: ",data,'from',addr_1

            s1.sendto(data,addr1_to)
            print "send data:",data, "to addr1_to:",addr1_to

            if data == '0':
                show_local[0] = True
                show_local_camera0[0] = True
                recieve_video[0] = False
                # print "show_local = ",show_local[0],"recieve_video = ",recieve_video[0]
            elif data == '2':
                show_local[0] = True
                show_local_camera0[0] = False
                recieve_video[0] = False
                # print "show_local = ",show_local[0],"recieve_video = ",recieve_video[0]
            elif data == '4' or data == '6' or data == '8':
                show_local[0] = False
                show_local_camera0[0] = False
                recieve_video[0] = True
                # print "show_local = ",show_local[0],"recieve_video = ",recieve_video[0]
            else:# default
                show_local[0] = True
                show_local_camera0[0] = True
                recieve_video[0] = False
                # print "show_local = ",show_local[0],"recieve_video = ",recieve_video[0]

thread.start_new_thread(data_thread,("data_thread",1))

while True:

    if show_local[0] and show_local_camera0[0] and not recieve_video[0]:# display local camera video
        # 打时间戳
        # dt = datetime.datetime.now()
        # cv2.putText(frame0,str(dt),(10,frame0.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX\
        # ,1.35,(0,0,255),1)
        cv2.imshow('show',frame0)
        cv2.waitKey(1)
    elif show_local[0] and not show_local_camera0[0] and not recieve_video[0]:
        # 打时间戳
        # dt = datetime.datetime.now()
        # cv2.putText(frame1,str(dt),(10,frame1.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX\
        # ,1.35,(0,0,255),1)
        cv2.imshow('show',frame1)
        cv2.waitKey(1)
    elif recieve_video[0] and not show_local[0] and not show_local_camera0[0]:
        max_size = 60000
        while True:
            if not recieve_video[0]:
                break
            stringdata,address = s2.recvfrom(max_size)
            while True:
                if not recieve_video[0]:
                    break
                # the last splice
                if len(stringdata) == 0:
                    if img_to_read != '':
                        img_to_show = img_to_read
                        img_to_read = ''
                    # print "receive one frame"
                    break
                # the last splice
                if (len(stringdata)<max_size) and (len(stringdata)>0):
                    img_to_read += stringdata
                    img_to_show = img_to_read
                    img_to_read = ''
                    # print "receive one frame"
                    # print 'len = %r' %len(img_to_show)
                    break
                img_to_read += stringdata
                stringdata,address = s2.recvfrom(max_size)

            data_show = np.fromstring(img_to_show,dtype=np.uint8)
            # print data_show
            # print data_show[0]
            # print data_show[(len(data_show)-2):]
            # checking if the frame is a standard jpeg picture
            # if it is a standard jepg picture,
            # the first 2 byte will be 0xFF 0xD8, the last 2 byte will be 0xFF 0xD9
            if data_show[0]==0xff and data_show[1]==0xd8 and \
            data_show[len(data_show)-2]==0xff and data_show[len(data_show)-1]==0xd9:
                # print len(data_show)
                # decode the data
                img_decoded = cv2.imdecode(data_show,1)
                # print img_decoded

                # 打时间戳
                # dt = datetime.datetime.now()
                # cv2.putText(img_decoded,str(dt),(10,img_decoded.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX\
                # ,1.35,(0,0,255),1)
                cv2.imshow('show',img_decoded)
                cv2.waitKey(1)
            else:
                # 打时间戳
                # dt = datetime.datetime.now()
                # cv2.putText(frame0,str(dt),(10,frame0.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX\
                # ,1.35,(0,0,255),1)
                cv2.imshow('show',frame0)
                cv2.waitKey(1)
    ret,frame0 = cap0.read()
    ret,frame1 = cap1.read()
    out0.write(frame0)
    out1.write(frame1)

cap0.release()
cap1.release()
s1.close()
s2.close()
s3.close()
