# 读写文本数据
# 问题：你需要读写不同编码的文本数据，比如ASCII等
# 解决方案：使用带有rt模式的open()函数来读取文本，使用带有wt模式的open()函数来写入文本

with open('./file/file1.txt', 'rt') as f:
    data = f.read()  # 已经到文件尾部，后面再用f读的话将读不到任何数据
    print(data)
    for line in f:
        print(line)  # 读不到任何数据

with open('./file/file1.txt', 'wt') as f:
    f.write("ababababbab")

# 打印输出到文件中
# 问题：你想将print()函数的输出重定向到一个文件中区
# 解决方案：在print中指定file关键字参数
with open('./file/file1.txt', 'wt') as f:
    print("print to file", file=f)

# 使用其他分隔符或行终止符打印
# 问题：你想使用print()函数输出数据，但是想改变默认的分隔符或者行尾符
# 解决方案：可以在print()函数中使用sep和end关键字参数，以你想要的方式输出
print(1, 2, 3)  # 1 2 3
print(1, 2, 3, sep=',')  # 1,2,3
print(1, 2, 3, end='!\n')  # 1 2 3!

# 文件不存在才能写入
# 问题：你想像一个文件中写入数据，但是前提是这个文件在文件系统中不存在。也就是不允许覆盖已存在的文件的内容
# 解决方案：可以在open()函数中使用x模式来代替w模式的方法来解决这个问题
# with open('./file/file1.txt', 'xt') as f:
    # f.write("bobo")  # 将会报错

# 模拟文件操作
# 问题：在测试单元中，需要一个文件对象
# 解决方法：可以使用io.StringIO()和io.BytesIO()类来创建文件对象操作字符串数据
import io
s = io.StringIO()
s.write("hello worlf!")
print("This is a test", file=s)
print(s.getvalue())  # hello worlf!This is a test
# 注意：io.StringIO()只能用于文本，如果你要操作二进制数据，要使用io.BytesIO类来代替
# 当你想模拟一个普通的文件的时候SringIO和BytesIO类很好用。比如在测试单元中，你可以使用StringIO来创建一个包含测试数据的类文件对象

# 读写压缩文件
# 问题：你想读写一个gzip或bz2格式的压缩文件
# 解决方案：gzip和bz2模块可以很容易的处理这些文件。两个模块都为open()函数提供了另外的实现来解决这个问题。
import gzip
import bz2
with open('./file/zip_test.gz', 'wt') as f:
    f.write("bobo")
with open('./file/bz_test.bz2', 'wt') as f:
    f.write('bz2 test')
with open('./file/zip_test.gz', 'rt') as f:
    text = f.read()
    print(text)