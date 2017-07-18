# coding:utf-8

# 字典排序
# 问题：你想创建一个字典，并且在迭代或序列化的时候希望可以控制元素的顺序
# 解决方案：使用collections模块中的OrderedDict类

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])
# OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])
print(d)

# 假如想精确控制以json编码后字段的顺序，你可以先使用OrderedDict来构建
import json
j = json.dumps(d)
# <class 'str'> {"foo": 1, "bar": 2, "spam": 3, "grok": 4}
print(type(j), j)

# 删除序列中相同的元素并保持顺序
# 问题：怎么在一个序列上面保持元素顺序的同时消除重复的值？
# 如果序列为Hashable类型，可以用集合或生成器解决：
def dedupe(item):
    seen = set()
    for it in item:
        if it not in seen:
            yield it
            seen.add(it)

a = [1, 2, 3, 2, 4, 6, 5, 6]
b = dedupe(a)
# [1, 2, 3, 4, 6, 5]
print(list(b))
# [1, 2, 3, 4, 5, 6] 改变了顺序，不行
b = set()
for i in a:
    if i not in b:
        b.add(i)
b = list(b)
print(b)