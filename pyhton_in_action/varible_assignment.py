#coding:utf-8

# 精确的引入某个模块中所需的东西
from math import sqrt,pi
# 注意，如果你后续引入的模块的函数与上面引用的函数同名，则会覆盖之

# 引入自己定义的模块
#import func

# **乘方的意思
ret = 2**5
print ret

#ret = func.add(2,2)
##print ret

# result qiucuber,但是这个方法不易理解
'qiu' 'cuber'
# result qiucuber,使用 + 号比较好一点。
'qiu'+'cuber'

# raw means it retruns as a string no matter what the user input
ret = raw_input('> ')
print "ret is string type"

# revert string to int
val = int(ret)
print "val is int type"

cap = "cuber"

# capitalize() 返回字符串首字母大写的副本
ret = cap.capitalize()
# result: cuber
print cap
# result: Cuber
print ret

# upper() 将所有字符串住那换为大写形式并返回
cap.upper()
# result:
print cap
# result:
print ret

# swapcase() 小写转大写，大写转小写
cap = ret.swapcase()
print ret
print cap
