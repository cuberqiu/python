import socket
import time
addr_to = ('127.0.0.1',9993)
addr_from = ('127.0.0.1',8883)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addr_from)
s.setblocking(0)

while True:
    s.sendto("33333333",addr_to)
    print "send mesg"
    data,addr_from1 = s.recvfrom(60000)
    if data:
        print "recvfrom:",data
    time.sleep(1)
s.close()
