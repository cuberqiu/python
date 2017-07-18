# coding:utf-8

# 保留最后N个元素

# 问题：迭代操作或者其他操作的时候，怎样只保留有限的几个元素的历史纪录？

# collections.deque

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# def return_test(start, end):
#     while start < end:
#         return start
#         # start = start + 1
#
# print(list(return_test(1, 10)))

def frange(start, stop):
    while start < stop:
        yield start
        start += 1

x = frange(1, 10)
print(type(x))
print(list(x))

# Python中yield的使用
# 带有yield的函数在python中称为生成器generator，不再是一个函数

# 生成一个裴波那契数列前N个数
def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L
# 该函数在运行的时候占用的内存回随参数max的增大而增大，如果要控制内存占用，最好不要用List来保存中间结果，而是通过iterable迭代
# 使用yield，函数会变成一个生成器，
def yab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
# 简单的讲，yield的作用就是把一个函数变成一个generator，带有yield的函数不再是一个普通函数
# Python解释器会将其视为一个generator，调用yab(5)不会执行fab函数，而是返回一个iterable的对象
# 在执行for循环时，每次循环会执行yab函数内部的代码，执行到yield b时，yab函数就返回一个迭代值，下次迭代时，代码从yield b的
# 下一条语句继续执行，而函数的本地变量看起来和上次终端执行前是完全一样的
for i in yab(5):
    print(i)

f = yab(5)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())


