# 可接受任意数量参数的函数
# 问题：你想构造一个可以接受任意数量参数的函数
# 解决方案：使用*参数来解决任意数量的 位置参数 ，使用**参数来解决任意数量的 关键字参数
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2, 3))  # 2.0
print(avg(1, 2, 3, 4))  # 2.5
# 在上述例子中，rest是有所有其他位置参数组成的元组

def key_para(key, value, **kwargs):
    key_value = [it for it in kwargs.items()]
    print(kwargs)
    print(key_value)

key_para(1, 2, x=1, y=2)
# 注意：*参数智能出现在函数定义中最后一个位置参数后面，而**参数只能出现在最后一个参数后面，*参数后面还可以定义其他参数

# 给函数增加元信息
# 问题：你写好了一个函数，然后想为这个函数增加一些额外的信息，这样的话其他使用者就能清楚的知道这个函数应该怎么使用。
# 解决办法：使用函数参数注解
def add(x:int, y:int) -> int: # ->指代要返回的类型
    return x + y

print(add(1, 10))

# 匿名函数捕获变量值
# 问题：使用lambda定义了一个匿名函数，并想在定义时捕获到某些变量的值
x = 10
a = lambda y: x+y  # lambda表达式中的x是一个自由变量，在运行时绑定值，而不是在定义时就绑定值，这跟函数的默认参数不同
x = 20
b = lambda y: x+y
print(a(10))  # 30
print(b(10))  # 30
x = 10
c = lambda y, x=x: x+y  # 让匿名函数在定义时就捕获到值，可以将那个参数定义成默认参数即可
print(c(10))  # 20

func = [lambda x: x+n for n in range(5)]
for f in func:
    print(f(0), end=' ')  # 4 4 4 4 4
print('\n')
func1 = [lambda x, n=n: x+n for n in range(5)]
for f in func1:
    print(f(0), end=' ')  # 0 1 2 3 4
print('\n')
