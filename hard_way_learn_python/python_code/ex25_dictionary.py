"""
    字典
    字典的没一个键值key=>value对用冒号分割，每个对之间用逗号分割，整个字典用花括号括起来
    键必须唯一，键值不一定唯一
"""

stuff = {'name':'Zed','age':36,'height':6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']

stuff['city']='San Francisco'
print stuff['city']

print stuff

stuff[1] = 'Wow'
stuff[2] = 'Neato'

print stuff[1]
print stuff[2]

print stuff

# 删除字典中的元素
del stuff['city']
del stuff[1]
del stuff[2]

print stuff

cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksovile'}
cities['NY'] = 'New York'
cities['OR'] = 'Porland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found!"

cities['_find'] = find_city

while True:
    print "State?(Enter to quit)",
    state = raw_input("> ")

    if not state:break

    city_found = cities['_find'](cities,state)
    print city_found

# 字典内置函数
Dict = {1:'a',2:'b',3:'c',4:'d',5:'e'}
# 计算字典的元素个数，即键的总数
print len(Dict)
# 输出字典可打印的字符表示
str_dict = str(Dict)
print str_dict
# 返回一个字典的浅复制
Dict_copy = Dict.copy()
print Dict_copy
Dict[1] = 'aa'
# result {1: 'aa', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print Dict
# result {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print Dict_copy
# 返回指定键的值，如果不存在则返回default值
# result aa
print Dict.get(1)
# result None
print Dict.get(10)
# 如果键在字典中，返回True
print Dict.has_key(1)
print Dict.has_key(10)
# 以列表返回可遍历的键值元组数组
ret = Dict.items()
# result [(1, 'aa'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
print ret
# 以列表返回一个字典所有的键
ret = Dict.keys()
# result [1, 2, 3, 4, 5]
print ret
# 以列表返回字典中所有值
ret = Dict.values()
# result ['aa', 'b', 'c', 'd', 'e']
print ret
Dict2 = {6:'f',7:'h'}
# 把字典dict2中的键/值更新到dict中，dict.update(dict2)
Dict2.update(Dict)
# result {1: 'aa', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'h'}
print Dict2
