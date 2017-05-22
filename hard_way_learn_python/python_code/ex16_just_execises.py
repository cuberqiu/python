#coding:utf-8
print "Let's practice everything."
print 'You\'d need to know\'bout escapes with \\ that do \n newlines and \t tabs.'

"""
    \(在行尾部)  续行符
    \\          反斜杠符号
    \'          单引号
    \"          双引号
    \a          响铃
    \b          退格
    \e          转义
    \000        空
    \n          换行
    \v          纵向制表
    \t          横向制表
    \r          回车
    \f          换页
"""
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-----------------------------"
print poem
print "-----------------------------"

five = 10-2+3-6
print "This should be five: %s" %five

# 定义
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print "With a starting point of :%d" %start_point
print "We'd have %d beans, %d jars, and %d crates." %(beans,jars,crates)

start_point = start_point/10

print "We cna also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." %secret_formula(start_point)
