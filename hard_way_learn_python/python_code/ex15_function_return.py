#coding:utf-8

#ADD function
def add(a,b):
    print "ADDING %d + %d" %(a,b)
    return a+b

# Subtract
def subtract(a,b):
    print "Subtract %d + %d" %(a,b)
    return a-b

# Multiply
def multiply(a,b):
    print "Multiply %d * %d" %(a,b)
    return a*b

# Divide
def divide(a,b):
    print "Divide %d / %d" %(a,b)
    return a/b

print "Let's do some math with just functions."

a = add(10,5)
s = subtract(10,5)
m = multiply(10,5)
d = divide(10,5)

print "a = %r, s = %r, m = %r, d = %r" %(a,s,m,d)
