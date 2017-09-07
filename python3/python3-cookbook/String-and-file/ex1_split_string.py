#coding:utf-8

# 使用多个界定分割字符串

# 问题1：将一个字符串分割为多个字段，但是分割符并不是固定的
# 解决方案：
"""
    string对象的split()方法只适应于非常简单的字符串分割情形，它并不允许有多个分隔符或者分割符周围不确定的空格
    当你需要更加灵活的切割字符串的时候，最好使用re.split()方法：
"""
line = 'asdf fjdk;   afed, fjek,asdf, foo      '
import re
# 分割line，分隔符可以是分号、逗号、空格,以及后面紧跟着任意空格
# <class 'list'> ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo', '']
ret = re.split('[;,\s]\s*', line)
print(type(ret), ret)
# 使用括号捕获分组，那么匹配的文本也将出现在列表中
ret = re.split('(;|,|\s)\s*', line)
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo', ' ', '']
print(ret)
# 如果不想保留分割字符串到结果列表中区，但仍需要使用到括号来分组正则表达式的话，确保你的分组是非捕获分组，形如(?:...)
ret = re.split('(?:,|;|\s)\s*', line)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo', '']
print(ret)


# 字符串开头或结尾匹配
# 问题2：你需要通过制定的文本模式去检查字符串的开头或结尾，比如文件名猴嘴，URL等等
# 解决方案：
"""
    检查字符串开头或者结尾的一个简单方法是使用str.startswith()或者是str.endswith()
"""
filename = "bobo.txt"
print(filename.endswith('txt'))
print(filename.startswith('bobo'))
# 如果你想检查多种匹配的可能，只需要将所有的匹配项放入到一个元组中去，然后给statswith()或者endswith()方法
import os
filename = os.listdir('.')
print(filename)
ret = [name for name in filename if name.endswith(('.py', '.txt'))]
print(ret)
print(any(name.endswith('.py') for name in filename))


# 用shell通配符匹配字符串
# 问题3：你想使用Unix Shell 中常用的通配符去匹配文本字符串
# 解决方案：
"""
    fnmatch模块提供了两个函数————fnmatch()和fnmatchcase()，可以用来实现这一的匹配。
"""
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('bobo.txt', '*.txt'))
print(fnmatch('bobo.txt', '*bo.txt'))
print(fnmatch('bobo.txt', 'b*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
ret = [name for name in names if fnmatch(name, 'Dat*')]
print(ret)
# 注意：fnmatch()函数使用底层操作系统的大小写敏感规则来匹配模式，所以不同操作系统不一样
# 如果你对大小写区别很在意，可以使用fnmatchcase()来代替。它完全遵循大小写区别
# True
# False
print(fnmatch('bobo.txt', '*.Txt'))
print(fnmatchcase('bobo.txt', '*.Txt'))


# 字符串搜索和替换
# 问题4：你想在字符串中搜索和匹配指定的文本模式
# 解决方案：
"""
    对于简单的字面模式，直接使用str.replace()方法即可
"""
text = 'yeah, but no, but yeah, but no, but yeah'
ret = text.replace('yeah', 'bobo')
# bobo, but no, but bobo, but no, but bobo
print(ret)
# yeah, but no, but yeah, but no, but yeah
print(text)  # 并没有改变text本身，仅仅是返回一个改变之后的字符串

# 对于复杂的模式，可以使用re模块中的sub()函数，例如想将11/27/2012的日期字符串改成2012-11-27:
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
# 字符串前加 r ，代表这个字符串是raw string，不能转义\*之类的
ret = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)  # \3代表向前面模式的捕获组号，即第三个
# Today is 2012-11-27. PyCon starts 2013-3-13.
print(ret)
# Today is 11/27/2012. PyCon starts 3/13/2013.
print(text)  # re.sub并没有改变text，仅仅是返回一个改变之后的字符串

# 忽略大小写的搜索和不忽略的搜索
ret = re.findall('today', text)
print(ret)  # []
ret = re.findall('today', text, flags=re.IGNORECASE)
print(ret)  # ['Today']

# 忽略与不忽略的搜索替换
ret = re.sub('today', 'yesterday', text)
print(ret)  # Today is 11/27/2012. PyCon starts 3/13/2013.
ret = re.sub('today', 'yesterday', text, flags=re.IGNORECASE)
print(ret)  # yesterday is 11/27/2012. PyCon starts 3/13/2013.

# 删除字符串中不需要的字符
s = '----hello world==='
ret = s.strip()  # strip()只会删除空白字符串
print(ret)  # hello world
print(s)  #  hello world  原s并没有改变，只是返回一个值
ret = s.lstrip('-')
print(ret)  # hello world===
ret = s.rstrip('=')
print(ret)  # ----hello world

# 字符串对齐
text = 'hello'
ret = format(text, '*>10')
print(ret)  # *****hello
ret = format(text, '*<10')
print(ret)  # hello*****
ret = format(text, '*^10')
print(ret)  # **hello***

# 字符串的拼接
# 解决方法 + 或者join()，不过join()比 + 快
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(" ".join(parts))  # Is Chicago Not Chicago?
print(",".join(parts))  # Is,Chicago,Not,Chicago?
# 需要注意的是，在使用加号来连接大量字符串的时候是非常低效率的，因为加号连接会引起内存复制以及垃圾回收操作！！
# 最好还是用join()
data = ["bobo", 1, 2]
ret = ''.join(str(it) for it in data)
print(ret)  # bobo12


