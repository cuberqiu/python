# coding:utf-8
# 手动遍历迭代器
# 遍历一个可迭代对象中的所有元素，但是却不用for循环
# 为了手动遍历可迭代对象，使用next()函数U币能够在代码中捕获StopIteration异常

with open('../../logging.log') as f:
    while True:
        num = next(f, None)
        if num == None:
            break
        print(num)

if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]
    it = iter(items)
    print(next(it))  # 1
    print(next(it))  # 2


# 代理迭代
# 构建一个自定义容器对象，里面包含有列表、元组或者其他可迭代对象。你想直接在你的这个新容器对象上执行迭代操作。
# 实际上你只需顶一个__iter__()方法，将迭代操作代理到容器内的对象上去。
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def get_children(self):
        return self._children

if __name__ == '__main__':
    root = Node(0)
    c1 = Node(1)
    c2 = Node(2)
    root.add_children(c1)
    root.add_children(c2)

    print(root)
    # print(next(root))  # error

    print(root.get_children())

    for ch in root:
        print(ch)


# 使用生成器创建新的迭代模式
# 你想实现一个自定义迭代模式，跟普通的内置函数比如range(), reversed()不一样
# 如果你想实现一种新的迭代模式，使用一个生成器函数来定义它，下面是一个生产某个范围内浮点数的生成器：
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

# 为了使用这个函数，你可以用for循环或者使用其他可接受一个可迭代对象的函数
for n in frange(0, 4, 0.5):
    print(n)
print(list(frange(0, 4, 0.5)))  # [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]

# 一个函数中需要有一个yield语句即可将其转换成为一个生成器。
# 跟普通函数不同的是，生成器只能用于迭代操作。
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print("Done!")

c = countdown(2)
print(c)  # <generator object countdown at 0x000001E27FDEF308>
print(next(c))  # Starting to count from 2  # 2
print(next(c))  # 1
# print(next(c))  # StopIteration


# 方向迭代
# 你想反向迭代一个序列
# 使用内置的reversed()函数
a = [1, 2, 3, 4, 5]
print(reversed(a))
for x in reversed(a):
    print(x, end=' ')
# 反向迭代仅仅当对象的大小可以预先确定或者对象实现了__reversed__()的特殊方法时才能生效
# 如果两者都不符合，就必须先将对象转换成为列表
# 需要注意的是，如果可迭代对象元素很多的话，将其预先转换为一个列表需要消耗很大的内存
# 在自定义类上实现__reversed__()方法来实现方向迭代：
class Countdown:
    def __init__(self, start):
        self.start = start

    # forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
print('\n')
for r in reversed(Countdown(3)):
    print(r, end=' ')  # 1 2 3

print('\n')
for r in Countdown(3):
    print(r, end=' ')  # 3 2 1

# 迭代器切片
# 问题：你想得到一个由迭代器的切片对象，但是标准切片操作并不能做到
# 解决方案：函数itertools.islice()正好适用于在迭代器和生成器上做切片操作
def count(n):
    while True:
        yield n
        n += 1
c = count(0)
# c[5:10]  # error

print('\n')
import itertools
for x in itertools.islice(c, 5, 10):
    print(x, end=' ')  # 5 6 7 8 9

# 跳过可迭代对象的开始部分
# 问题：你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们
# 解决方案：itertools模块中有一些函数可以完成这个任务，首先介绍的是itertools.dropwhile()函数。
# 使用时，给它传递一个函数对象和一个可迭代对象。
# 它会返回一个迭代对象，丢弃原有序列中直到函数返回False之前的所有元素，然后返回后面所有元素
from itertools import dropwhile
with open('../../logging.log') as f:
    for line in dropwhile(lambda l: l.startswith('C'), f):
        print(line)


# 排列组合的迭代
# 问题：你想遍历一个集合中元素的所有可能的排列组合
# 解决方案：itertools.permutations()和itertools.combinations()
from itertools import permutations, combinations
items = [1, 2, 3]
for p in permutations(items):
    print(p)
print('...........')
for c in combinations(items, 3):
    print(c)  # (1, 2, 3) 重复的不会出现, (1, 2) 和 (2, 1)是一样的

for c in combinations(items, 2):
    print(c)  # (1, 2) (1, 3) (2, 3)

# 同时迭代多个序列
# 问题：你想同时迭代多个序列，每次分别从一个序列中取一个元素
# 解决方案：使用zip()函数
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd', 'e']
for x, y in zip(a, b):
    print(x, y)

from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)
for i in zip_longest(a, b, fillvalue=0):
    print(i)

# 不同集合上元素的迭代
# 问题：你想在多个对象上执行相同的操作，但是这些对象在不同的容器中，你希望代码在不丢失可读性的情况下避免写重复的循环。
# 解决方案：iterstools.chain()防范可以用来简化这个任务。
# 它接受一个可迭代对象列表作为输入，并返回一个迭代器，有效的屏蔽掉在多个容器中迭代细节
# 使用chain()的一个常见场景是你想对不同的集合中的所有元素执行某些相同操作的时候
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    # prcess the elements in a and b
    print(x)  # 会依次遍历a, b中所有的元素

# 创建数据处理管道
# 问题：你想以数据管道的方式迭代处理数据，比如你有大量的数据需要处理，但是不能将它们一次性放入内存中。
# 解决方案：生成器函数是一个实现管道机制的好办法。

# 展开嵌套的序列
# 问题：你想将一个多层嵌套的序列展开成一个单层列表
# 可以使用一个包含yield from语句的递归生成器轻松解决这个问题
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]

x = flatten(items)
print(list(x))  # [1, 2, 3, 4, 5, 6, 7, 8]
# yield from 在你想在生成器中调用其他生成器作为子例程的时候非常有用
