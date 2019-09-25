from IPy import IP

ip = IP('127.0.0.0/30')

print(ip)

class A:
    def add(self):
        return 1
    def sub(self):
        return 2

from traitlets import Any

x = Any(a=A(),b=2,c=3,d=4)

print(x.add())