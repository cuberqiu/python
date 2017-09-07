# coding:utf-8

# 数字的四舍五入
# 对浮点数执行指定精度的舍入运算

# 对于简单的舍入运算，使用内置的round(value, ndigits)函数即可, 后面一个参数代表保留几位数
print(round(1.23, 1))  # 1.2
print(round(1.27, 1))  # 1.3
print(round(-1.23, 1))  # -1.2
print(round(-1.27, 1))  # -1.3
print(round(1.253, 2))  # 1.25

# 当一个值刚好在两个边界中间的时候，round函数回返回离它最近的偶数
print(round(1.5, 0))  # 2.0
print(round(2.5, 0))  # 2.0

# round()函数中的ndigits参数可以传入负数，这种情况下回作用在十位、百位、千位上
print(round(25.23, -1))  # 30.0
print(round(23.23, -2))  # 0.0
print(round(124.2, -1))  # 120.0

# 注意，不要讲舍入和格式化搞混淆了，如果目的只是简单的输出一指定宽度的数，就不需要使用round函数
x = 21.23456
print(format(x, '0.2f'))  # 21.23
print(format(x, '0.3f'))  # 21.235
print(format(x, '0.0f'))  # 21

# 执行精确的浮点运算
# 如果希望对浮点数执行精确的计算操作，并且不希望有任何小误差的出现。
# 浮点数的一个普遍问题是它们并不能精确的表示十进制数：
a = 4.2
b = 2.1
print(a+b)  # 6.300000000000001
print((a+b)==6.3)  # False
# 这是由于python的浮点数据类型使用底层表示存储数据，因此没有办法避免这样的误差

# 如果你想更加精确，并能容忍一定的性能损耗，你可以使用decimal模块
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)  # 6.3
print((a+b)==6.3)  # False
print((a+b)==Decimal('6.3'))  # True

nums1 = [1.23e+18, 1, -1.23e+18]
nums2 = [1.23e+18, -1.23e+18, 1]
print(sum(nums1))  # 0.0  大数运算时忽略了1
print(sum(nums2))  # 1.0  先做大数运算变成了小数，然后可以得到1
from math import fsum
print(fsum(nums1))  # 1.0 fsum提供更精确的计算能力

# 二八十六进制整数
# 问题：你需要转换或输出和使用二进制，八进制或十六进制表示的整数
# 为了将整数转换为二进制、八进制或十六进制的文本串，可以分别使用bin(),oct(),hex()函数
x = 1234
print(bin(x))  # 0b10011010010  0b为前缀
print(oct(x))  # 0o2322   0o为前缀
print(hex(x))  # 0x4d2   0x为前缀

# 另外，如果你不想输出0b 0o 0x的话，可以使用format()函数
print(format(x, 'b'))  # 10011010010
print(format(x, 'o'))  # 2322
print(format(x, 'x'))  # 4d2

# 复数的数学运算
# 复数可以使用函数complex(real, img)或者是带有后缀j的浮点数来指定。
a = complex(2, 4)
b = 3 - 5j
print(a)  # (2+4j)
print(b)  # (3-5j)
# 取实部、虚部和共轭复数可以很容易的获取
print(a.real)  # 2.0
print(a.imag)  # 4.0
print(a.conjugate())  # (2-4j)

# 所有常见的数学运算也可以做
print(a + b)  # (5-1j)
print(a * b)  # (26+2j)
print(a / b)  # (-0.4117647058823529+0.6470588235294118j)
print(abs(a))  # 4.47213595499958

# 对复数执行正弦余弦运算
import cmath
print(cmath.sin(a))  # (24.83130584894638-11.356612711218174j)
print(cmath.cos(b))  # (-73.46729221264526+10.471557674805572j)

# python中的无穷大与NaN(非数字)的浮点数
# Python中并没有特殊的语法来表示特殊的浮点值，但是可以用float()来创建它们
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)  # inf -inf nan
# 测试这些值的存在
import math
print(math.isinf(a))  # True
print(math.isnan(c))  # True
# NaN值会在所有操作中传播，NaN值之间的比较会返回False
d = float('nan')
print(c == d)  # False
print(c is d)  # False
# python中检测一个NaN值得唯一安全的方式就是使用math.isnan()

# Python中的分数运算
# fractions模块可以被用来执行包含分数的数学运算
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
c = a * b
print(a+b, a*b, a/b, c.numerator, c.denominator)  # 27/16 35/64 20/7 35 64

# 大型数组的运算
# 涉及到数组的重量级运算操作，可以使用Numpy库。
# Numpy库的一个主要特征是它会给Python提供一个数组对象，相比标准的python列表而言，更适合用来做数学运算
# python list
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print(x*2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(x + y)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax*2)  # [2 4 6 8]
print(ax + 2)  # [3 4 5 6]
print(ax + ay)  # [ 6  8 10 12]

# 随机选择
# random模块有大量的函数用来产生随机数和随机选择元素
# 从一个序列中随机抽取一个元素，使用random.choice()
import random
v = [1, 2, 3, 4, 5]
print(random.choice(v))  # 1
print(random.choice(v))  # 5
# 提取N个不同元素的样本，使用random.sample()
print(random.sample(v, 2))  # [3, 2]
print(random.sample(v, 3))  # [4, 3, 5]
# 打乱序列中的顺序，使用random.shuffle()
random.shuffle(v)
print(v)  # [1, 3, 4, 2, 5]
# 获取随机整数，random.randint()
print(random.randint(0, 5))
# 获得0到1之间均匀分布的浮点数，使用random.random()
print(random.random())
