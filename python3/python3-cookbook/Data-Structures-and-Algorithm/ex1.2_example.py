# coding:utf-8

# 解压可迭代对象赋值给多个变量

# 问题：如果一个可迭代的对象的元素个数超过变量个数时，会抛出ValueError，那该怎样从可迭代的对象中解压出N个元素呢？

# 解决方法：用*参数解决这个问题


def drop_first_last(seq):
    # 要去掉第一个和最后一个元素，只取中间元素：
    first, *mid, last = seq
    return mid

seq = [1, 2, 3, 4, 5]
str = "abcdef"
seq_after_drop = drop_first_last(seq)
str_after_drop = drop_first_last(str)
# result:[2, 3, 4]
#        ['b', 'c', 'd', 'e']
print(seq_after_drop)
print(str_after_drop)

# 扩展的迭代语法是专门为解压不确定个数或任意元素的可迭代对象而设计的。
# 值得注意的是，*表达式在迭代元素为可变长元组的序列时是很有用的。例如：
records = [('foo', 1, 2), ('bar', 3), ('foo', 3, 4)]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    if tag == 'bar':
        do_bar(*args)

# *在字符串操作时很有用，比如分割字符串
line = "bobo:anddfa:dfh:aiud:huahua"
myname, *_, name = line.split(':')
print(myname, name)

# 用*实现递归，不过递归并不是python所擅长的，因此不用太纠结递归
def sum(item):
    head, *tail = item
    return head + sum(tail) if tail else head

print(sum([1, 2, 3]))
