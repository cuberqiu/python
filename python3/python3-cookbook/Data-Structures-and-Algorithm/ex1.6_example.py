# coding:utf-8

# 字典中的键映射多个值

# 问题：怎样实现一个键对应多个值得字典(也叫Multidict)

# 一个字典就是一个键对应一个单值得映射。如果需要一个键映射多个值，就需要把多个值放在一个列表或集合之中
d = {'a': [1, 2, 3], 'b': [4, 5]}

# 简单的做法是使用collections模块中的defaultdict来构造字典。
from collections import defaultdict

d_list = defaultdict(list)
d_list['a'].append(1)
d_list['a'].append(2)
d_list['b'].append(4)
print(d_list)

d_set = defaultdict(set)
d_set['a'].add(1)
d_set['a'].add(2)
d_set['b'].add(4)
print(d_set)

# python中的集合set: 是一个无序的不重复元素的集合，因此不支持Index和slicing操作，支持x in set ,for x in set
x = set('hello')
# {'l', 'o', 'e', 'h'}
print(x)

# 去除海量列表中的重复元素
a = [1, 2, 3, 3, 5, 5, 9, 10, 9]
b = set(a)  # 此时，虽然已经去除重复元素，但是b是一个集合而不是列表，所以要转成列表
# {1, 2, 3, 5, 9, 10}
print(b)
a = [i for i in b]
# [1, 2, 3, 5, 9, 10]
print(a)
# 基本操作
b.add(11)  # 添加一项
# {1, 2, 3, 5, 9, 10, 11}
print(b)
b.update([1, 4, 6])  # 添加多项
# {1, 2, 3, 4, 5, 6, 9, 10, 11}
print(b)

