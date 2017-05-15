# Variables and names in python
#coding:utf-8
#如果后续的print中使用了中文，则需要 上面的定义

my_name = "bobo"
my_age = 23
my_height = 1.75

# Output : bobobobobobo
print my_name*3

# Output : bobohaha
print my_name + "haha"

# Output : my name is bobo ,and I am 23 years old,and my height is 1.75 m.
print "my name is",my_name,",and I am",my_age,"years old,and my height is",my_height,"m."

# Output : my name isbobo
print "my name is%s" %my_name

# Output : my name is bobo, my age is 23, my height is 1.75
# %r is a very useful one. It's like saying "print this no matter what."
print "my name is %s, my age is %d, my height is %r" %(my_name,my_age,my_height)

print """ heartcraft
what should i do ?"""

print "我是粗哟"
