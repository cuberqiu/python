# coding:utf-8

# 解压序列赋值给多个变量
# 问题：现有一个包含N个元素的元组或序列，怎样将它里面的值解压后同时赋给N个变量？

# 解决方案：任何序列可以通过一个简单的赋值语句解压并赋值给多个变量。
# 唯一的前提是变量的数量必须跟序列元素的数量是一样的！

p = (1, 2, 3)
a, b, c = p

# result:(1, 2, 3)
#         1 2 3
print(p)
print(a, b, c)

# 讨论，实际上这种解压赋值可以用子啊任何可迭代对象上面，而不仅仅是列表或元组，包括字符串，文件对象，迭代器和生成器
s = 'Hello'
a, b, c, d, e = s
# result: H e l l o
print(a, b, c, d, e)

# 有时候你可能只想解压一部分，丢弃其他的值，对于这种情况，python没有特殊的语法，但是可以使用任意变量名去占位。
data = ['bobo', 50, 30]
name, _, _ = data
print(name)
