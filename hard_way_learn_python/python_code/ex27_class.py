# coding:utf-8
# 创建一个类
class TheThing(object):
    # 为python class 设置内部变量的方式
    def __init__(self):
        self.number = 0

    def some_function(self):
        print "I got called."

    def add_me_up(self,more):
        self.number += more
        return self.number

# 两个不同的对象
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

class TheMultiplier(object):

    def __init__(self,base):
        self.base = base

    def do_it(self,m):
        return m*self.base

x = TheMultiplier(a.number)
print x.do_it(b.number)

# 一个简单的python类实例
class Employee:
    # 类变量，它的值将在这个类的所有实例之间共享。用Employee.empCount来调用
    empCount = 0

    # 构造函数或称初始化方法，当创建了这个类的实例就会调用该方法
    # self代表类的实例，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" %Employee.empCount

    def displayEmployee(self):
        print "Name: ",self.name, ", salary: ", self.salary

# 创建实例对象
emp1 = Employee("bobo",10000)
emp2 = Employee("binbin",20000)
print "Total Employee %d" %Employee.empCount
print Employee

# 访问实例
emp1.displayEmployee()
emp2.displayEmployee()

# 添加，删除，修改类的属性
emp1.age = 10 # 添加
emp1.age = 20 # 修改
del emp1.age  # 删除

# 也可以用以下方式来访问属性
"""
    getattr(obj,name[,deault]):访问对象的属性
    hasattr(obj,name):检查是否存在一个属性
    setattr(obj,name,value):设置一个属性。如果属性不存在，会创建一个新属性
    delattr(obj,name):删除属性
"""

hasattr(emp1,'age')  #如果存在'age'属性，返回true
hasattr(emp1,'name')
setattr(emp1,'age',100)  # 添加属性'age'，值为8
getattr(emp1,'age')  #返回属性的值
getattr(emp1,'name')
delattr(emp1,'age')  #删除属性'age'

# python内置类属性
"""
    __dict__: 类的属性
    __doc__ : 类的稳定那个字符串
    __name__:类名
    __module__: 类定义所在的模块
    __bases__:类的所有父类构成元素
"""

print Employee.__dict__
print Employee.__doc__
print Employee.__name__
print Employee.__module__
print Employee.__base__

# python中类的继承
"""
    python中继承的一些特点：
    1.在继承中基类的构造(__init__())不会被自动调用，它需要在其派生类的构造中亲自专门调用
    2.在调用基类的方法时，需要加上积累的类名前缀，且需要带上self参数变量。区别于在类中调用普通
      函数时并不需要带上self参数
    3.python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到积累中
      逐个查找。
    4.如果在继承元组中列了一个以上的类，那么它就被称作“多重继承”
"""
# 定义父类
class Parent:
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print "调用父类方法"

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性：",Parent.parentAttr

# 定义子类
class Child(Parent):
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print "调用子类方法child method"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

# 方法重写
class P():
    def myMthod(self):
        print "调用父类方法"

class C(P):
    def myMthod(self):
        print "调用子类方法"

c = C()
c.myMthod()
