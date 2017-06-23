import socket
import time
addr_to = ('127.0.0.1',9991)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = raw_input("> ")
    s.sendto(data,addr_to)
    print "send mesg:",data,"to",addr_to

s.close()
