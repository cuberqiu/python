from  datetime import *

def log(func):
    def wrapper(*args, **kwargs):
        print("call :" + func.__name__)
        return func(*args, **kwargs)

    return wrapper

@log
def now():
    print(datetime.now())

now()
print(now.__name__)  # wrapper


def argLog(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(text+" call "+func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@argLog('execute')
def argNow():
    print(datetime.now())

argNow()

import functools

def myDecorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call "+ func.__name__)
        return func(*args, **kwargs)
    return wrapper

@myDecorator
def myNow():
    print(datetime.now())

myNow()
print(myNow.__name__)  # myNow

print("......................")

def exeDecorator(func):
    print("begin call 1")
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("begin call 2")
        func(*args, **kwargs)
        for n in args:
            print(n , end=" ")

        print()
        print("after call")
        # return func(*args, **kwargs)
    return wrapper

@exeDecorator
def exeNow(a, b):
    print("exeNow :"+str(datetime.now()))
    print("value : ", a ,  b)

exeNow(1, 2)