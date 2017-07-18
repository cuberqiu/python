# coding:utf-8

# 实现一个优先级队列

# 问题：怎样实现一个优先级排序的队列？别切在这个队列上面每次pop操作总是返回优先级最高的哪一个元素
# 解决方案：使用heapq模块实现一个简单的优先级队列

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # 保证同等优先级的元素正确排序

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

q = PriorityQueue()
q.push('foo', 1)
q.push('bar', 2)
q.push('too', 3)

print(q.pop())
print(q.pop())

# 通过使用三元组(priority, index, item)，就能避免同优先级的元素的正确比较
# Python在做元组比较时，如果前面的比较已经可以确定结果，后面的比较操作就不会发生
a = (1, 0, 'foo')
b = (5, 3, 'bar')
c = (1, 2, 'too')
print(a < b)
print(a < c)

# 字典的运算
# 问题：怎样在数据字典中执行一些计算(比如求最大值，最小值，排序等)
# 使用zip()反转键与值
prices = {'foo': 1, 'bar': 2, 'spam': 3}
min_price = min(zip(prices.keys(), prices.values()))
max_price = max(zip(prices.values(), prices.keys()))
# ('bar', 2) (3, 'spam')
print(min_price, max_price)
# {'spam': 3, 'bar': 2, 'foo': 1}, 并未改变prices本身
print(prices)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# [(1, 'foo'), (2, 'bar'), (3, 'spam')]
print(prices_sorted)
# 需要注意的是，zip()函数创建的是只能访问一次的迭代器
zip_ret = zip(prices.keys(), prices.values())
print(min(zip_ret))  # ok
# print(max(zip_ret))  # error

# 注意，min或max直接作用于字典是，会比较键而不是值
# bar
print(min(prices))
# 如果zip之后，键值相等，则会根据键的大小来比较返回

# 查找两个字典的相同点
# 问题：怎样查找两个字典中相同点，比如相同的键、相同的值等
a = {'x': 1, 'y': 2, 'z': 3}
b = {'x': 10, 'y': 2, 'w': 3}

# {'x', 'y'}
# {'z'}
# {('y', 2)}
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
# <class 'dict_items'>
print(type(a.items()))
