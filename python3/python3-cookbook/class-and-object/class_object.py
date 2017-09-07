# 改变对象的字符串显示
# 问题：你想改变对象实例的打印或显示输出，让它们更具可读性
# 解决方案：要改变一个实例的字符串表示，可以重新定义它的__str__()和__repr__()方法
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self): # 0是self本身呢
        return "Pair({0.x!r}, {0.y!r})".format(self)  # !r格式化代码指明输出使用__repr()__来代替默认的__str__()
    def __str__(self):
        return "({0.x!s}, {0.y!s})".format(self)

p = Pair(3, 4)
print(p)
print("{0!r}".format(p))  # 0 是self本身，!r代表格式化代码，指明输出使用__repr__()
# 如果__str__()没有被定义，那么就会使用__repr__()

# 让对象支持上下文管理协议
# 问题：你想让你的对象支持上下文管理协议(with语句)
# 解决方案：为了让一个对象兼容with语句，你需要实现__enter__()和__exit__()方法

class LazyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __enter__(self):
        print("enter function is called!")
        x = LazyClass(self.a, self.b)
        return x
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit function is called!")

# enter function is called!
# 1 2
# exit function is called!
with LazyClass(1, 2) as c:
    print(c.a, c.b)
# 编写上下文管理器的主要原因是你的代码会放到with语句块中执行。当出现with语句的时候，对象的__enter__()方法被触发
# __enter__()的返回值会被赋给as声明的变量， 退出with块时，__exit__()方法会被触发进行清理工作

# 创建大量的对象时节省内存的方法
# 问题：你的程序需要创建大量的对象，导致占用很大的内存
# 解决方案：对于主要是用来当成简单的数据结构的类来讲，你可以通过给类添加__slots__属性来极大的减少实例所占用的内存
class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# 当你定义__slots__后，Python就会为实例使用一种更加紧凑的内部表示。
# 实例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典。
# 使用__slots__后，我们就只能使用__slots__中列出的属性，而不能再添加其他属性。
# 需要注意的是，使用__slots__后，很多普通类的特性就不支持了，比如继承啥的

# 在类中封装属性名
# 问题：你想封装类的实例上面的私有数据，但是Python语言并没有访问控制
# 解决方法：Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果，
# 单下划线开头的名字都应该在类内部实现，包括变量和方法
class A:
    def __init__(self):
        self._internal = 0  # 私有变量
        self.public = 1 # 公有变量
    def _private_method(self):
        print("A private method")
        pass
    def public_method(self):
        print("self._internal=%d" % self._internal)
        self._private_method()
class SubA(A):
    def __init__(self):
        self._internal = 1
        self.public = 2
    def _private_method(self):
        print("Sub A private method")


# 双下划綫开头的命名
class B:
    def __init__(self):
        self.__internal = 1
    def __private_method(self):  # 不会被子类重写
        print("B private method")
        pass
    def public_method(self):
        print("self.__internal=%d"%self.__internal)
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__internal = 2 # 不会覆盖B.__interbal
    def __private_method(self): # 不会覆盖父类同名方法
        print("C private method")

suba = SubA()
c = C()
suba.public_method()  # self._internal=1 Sub A private method
c.public_method()  # self.__internal=1 B private method

# 简言之，前缀单下划线和双下划线都表示私有变量，但是双下划綫不会被子类重写
# 机制：使用双下划綫前缀会到之后访问名称变成其他形式，比如在B类中，私有属性会被分别重命名为_B_internel和_B_private_method,
# C中则会被重命名为_C_internel和_C_private_method

# 创建可管理的属性
# 问题：你想某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证
# 解决方案：自定义某个属性的一种简单方法是将它定义为一个property
class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value
    @first_name.deleter
    def first_name(selfs):
        raise AttributeError("Can't delete attribute")
# 上述代码中有三个关联的方法，这三个方法的名字都必须一样。
# 第一个方法是一个getter函数，它使得first_name成为一个属性。其他两个方法给first_name属性添加了setter和deleter函数。
# 需要注意的是：只有在first_name属性被创建后，后面得两个装饰器才能被定义
# property的一个关键特征是它看上去跟普通的atrribute没有什么两样，但是访问它的时候会自动触发getter、setter和deleter方法
# 一个property属性其实就是一系列相关绑定方法的集合。
a = Person('bobo')
print(a.first_name)  # bobo 注意，不需要()
# a.first_name = 40  # error TypeError: Expected a string
# del a.first_name  # error AttributeError: Can't delete attribute

