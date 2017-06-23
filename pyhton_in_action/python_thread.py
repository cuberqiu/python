import thread
import time
import serial
import cv2



a = ['n']
def mythread1(threadname,num):
    while True:
        a[0] = raw_input("> ")
        print "a[0] = %r"%a[0]

def mythread2(threadname,num):
    while True:
        if a[0]=='0':
            print "0000000"
            a[0]='n'
        elif a[0]=='1':
            print "1111111"
            a[0]='n'
        else:
            pass

thread.start_new_thread(mythread1,("video thread1",1))
thread.start_new_thread(mythread2,("video thread2",2))


while True:
    pass
