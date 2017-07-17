# coding:utf-8


# python 中访问字符串中的值
str1 = "This is python3"

print(str1[1])
print(str1[1:5])

# 字符串更新

str1 = str1[:5]+"这是更新部分"
print("更新之后的str1= ", str1)

# Python 中的转义字符
print("这是换行符\n，这是反斜杠符号\\，这是单引号\'，这是双引号\",这是响铃\a,这是退格符号\b，这是回车\r，")

# Python中字符串格式化
# print("这是格式化字符及其ASCII码 %c ",
#       "这是格式化字符串%s",
#       "这是格式化整数%d",
#       "这是格式化无符号八进制数%o",
#       "格式化无符号十六进制%x" % ('c', "bobo", 10, 7, 26))


# 格式化输出
name = "cuberqiu"
age = 23

print("{} is a boy.".format(name))
print("{} is {} years old.".format(name,age))

# locals()与globals()的区别：基于字典的局部和全局的访问方式
def test(arg):
    z = 1
    print(locals())
    return "the arg is {arg}, and the local variable is {z}".format(**locals())

# locals()返回局部变量的和传入参数的字典
ret = test("bobo")
print("locals()的结果：", ret)

# globals()返回所有的全局变量的字典
print("globals()的结果：", globals())

text = "the arg is {arg}, and the local variable is {z}"
print(text.count('the', 0, len(text)))
text = "abcdefg"
print(text.center(3))
print(text.capitalize())

# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1, 2))

x = int(2.9) # 内建作用域

g_count = 0 # 全局作用域
def outer():
    o_count = 1 # 闭包函数外的作用域
    def inner():
        i_count = 2 # 局部作用域

# global和nonlocal关键字
# 修改全局变量需要提前用global声明
num = 1
def func1():
    global num # 需要使用global关键字声明才能修改它
    print(num)
    num = 123
    print(num)

func1()

# 修改嵌套作用域中的变量需要nonlocal声明
def outer():
    num = 10
    def inner():
        nonlocal num # nonlocal 声明
        num = 100
        print(num)
    inner()
    print(num)

# outer()

str1 = "2012%43423"
print(str1)

import time
x = [1,2,3,3,3,5,2,3,5,2,3]

while True:
    for i in range(len(x)):
        if x[i] == 2:
            break
    time.sleep(1)
    print("cycle")


