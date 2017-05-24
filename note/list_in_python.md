# list在python中的使用

```python
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff)!=10:
    next_one = more_stuff.pop()
    print "Adding :",next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go:",stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff[0:2]
print stuff.pop()
print stuff

# 用‘ ’来连接stuff,但连接之后，连接符并不当作元素
print ' '.join(stuff)
print '#'.join(stuff)
print len(stuff),stuff[2]

# 列表
list1 = [1,2,3,4,5,6,7,8,9,10]
print list1
# 删除列表中某一个元素
del list1[0]
print list1
# 计算list的长度
print len(list1)

# +用于组合列表，*用于重复列表
num1 = [1,2,3]
num2 = [4,5,6,7]
add_num = num1 + num2
print add_num
multi_num = num1*2
print multi_num

# 判断一个元素是否在列表中
print 3 in num1
print 3 in num2

# for 遍历列表
for x in add_num:
    print x,

# 列表元素截取
# 第二个元素
print add_num[1]
# 最后一个元素
print add_num[-1]
# 倒数第二个元素
print add_num[-2]
# 第二个及其以后的元素
print add_num[1:]

# 列表函数
# 比较两个列表的元素
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [2,3,4]
l4 = [0,1,2]
cmp(l1,l2)
cmp(l1,l3)
cmp(l1,l4)
# 返回列表最大值
print max(l1)
# 返回列表最小值
print min(l1)
# 将元组转换成列表

# 列表包含的方法
# 在列表末尾添加新的对象,只能添加一个对象
l = [1,2,2,3,3,3]
l.append(4)
# result [1, 2, 2, 3, 3, 3, 4, 4]
print l
l.append(l1)
# result [1, 2, 2, 3, 3, 3, 4, 4, [1, 2, 3]]
print l
# 移除列表中的一个元素，默认为最后一个
l.pop()
# result [1, 2, 2, 3, 3, 3, 4]
print l
l.pop(0)
# result [2, 2, 3, 3, 3, 4]
print l
# 统计某个元素在列表中出现的次数
count = l.count(3)
print count
# 在列表的末尾一次性最佳另一个序列中的多个值
l.extend(l1)
# result [2, 2, 3, 3, 3, 4, 1, 2, 3]
print l
# 在列表中找到某个值第一次匹配项的索引位置
print l.index(2)
# 将一个对象插入列表,insert(index,obj)
l.insert(0,1)
# result [1, 2, 2, 3, 3, 3, 4, 1, 2, 3]
print l
# 移除列表中某个值的地一个匹配项
l.remove(2)
# result [1, 2, 3, 3, 3, 4, 1, 2, 3]
print l
# 反向列表中的元素
l.reverse()
# result [3, 2, 1, 4, 3, 3, 3, 2, 1]
print l
# 对列表中的元素进行排序
l.sort()
# result [1, 1, 2, 2, 3, 3, 3, 3, 4]
print l

```
