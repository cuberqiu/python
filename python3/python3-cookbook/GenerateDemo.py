"""
生成器Generator：在需要大量数据时，例如很长的列表，为了节省内存，采用一种一边循环一边计算的方法，就是生成器
"""
L = [x*x for x in range(10)]

print(L)

L_generator = (x*x for x in range(10))

# 0 1 4 9
print(next(L_generator), end=" ")
print(next(L_generator), end=" ")
print(next(L_generator), end=" ")
print(next(L_generator))

# 16 25 36 49 64 81
for n in L_generator:
    print(n, end=" ")

print()


# 斐波拉切数列 函数版本
def fib(max):
    a, b = 0, 1
    while max >=0:
        print(b, end=" ")
        a, b = b, a+b
        max = max - 1
    return "done"


fib(5)
print()

# 斐波拉切数列 生成器版本
def fib_generator(max):
    a, b = 0, 1
    while max>=0:
        yield b
        a, b = b, a+b
        max = max - 1
    return "done"

for n in fib_generator(5):
    print(n, end=" ")

# 通常使用生成器时需要捕获StopIteration的异常
g = fib_generator(6)
print()

while True:
    try:
        print(next(g), end=" ")
    except StopIteration as e:
        print(e.value)
        break


# 杨辉三角
def triangle(row):
    a, b, n = [], [1], 1
    while row>0:
        yield b
        a = b
        b = [1]
        n = 1
        while n < len(a):
            b.append(a[n]+a[n-1])
            n = n+1
        b.append(1)
        row = row - 1

for n in triangle(10):
    print(n)


