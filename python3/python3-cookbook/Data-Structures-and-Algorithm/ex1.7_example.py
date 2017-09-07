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

# 命名切片
# 问题：你的程序已经出现大堆无法直视的硬编码切片下标，然后你想清理下代码

record = '......100.....2...'
cost = int(record[6:9])
print(cost)

COST = slice(6, 9)
cost = record[COST]
print(cost)

# slice创建一个切片对象，可以被用在任何允许切片的地方

item = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = slice(1, 3, 7)
print(a.start)
print(a.stop)
print(a.step)

# 找出序列中出现次数最多的元素
# 解决方案collections.Counter类就是专门为这类问题设计的，

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的单个单词
top_three = word_counts.most_common(3)
print(type(top_three), top_three)
# 作为输入，Counter对象可以接受任意的由可哈希元素构成的序列对象
# 在底层实现上，一个Counter对象就是一个字典，将元素映射到出现的次数上
print(word_counts['eyes'])

# 通过某关键字对排序一个字典列表
# 问题：你有一个字典列表，你想根据某个或某几个字典段来排序这个列表
# 解决：通过使用operator模块的itemgetter函数，可以非常容易的排序这样的数据结构
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# 排序不支持原生比较的对象
class User:
    def __init__(self, user_id):
        self.user_id = user_id

from operator import attrgetter
users = [User(1), User(3), User(2)]
print(sorted(users, key=attrgetter('user_id')))

# 通过某个字段将记录分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# 现在假设想按date分组后的数据块上进行迭代。
# 为了这样做，需要先按照指定的字段排序，然后调用itertools.groupby()函数
from operator import itemgetter
from itertools import groupby

# sorted by the desired field first
rows.sort(key=itemgetter('date'))
print(rows)
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# groupby()函数回扫描整个序列并查找连续相同值得元素序列。
# 在每次迭代的时候，会返回一个值和一个迭代对象，这个迭代对象可以生产元素值全部等于上面那个值的组中的所有对象
# 一个非常重要的准备步骤是要根据指定的字段将数据排序，因为groupby()仅仅检查连续的元素，
# 如果事先没有排序的话，分组函数将得不到想要的结果

# 如果仅仅是想根据date字段将数据分组到一个大的数据结构中区，并且允许随机访问，那么最好使用defaultdict()来构建多值字典
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

print(rows_by_date)

# 过滤序列元素
# 最简单的方法就是用序列推导
mylist = [1, 4, -6, 10, 2, 3, -1]
filter_list = [n for n in mylist if n > 0]
# [1, 4, 10, 2, 3]
print(filter_list)
# 序列推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量的内存。
# 如果对内存比较敏感，那么可以使用生成器表达式迭代产生过滤的元素。
pos = (n for n in mylist if n > 0)
# <generator object <genexpr> at 0x00000161AC4EAA98>
print(pos)
# 有时候，过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中白殴打出来。
# 这个时候可以将过滤代码放到一个函数中，然后使用内建的filter函数
values = [1, 2, 3, 4, 5, '-', 6]
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
# [1, 2, 3, 4, 5, 6]
print(ivals)
# filter函数创建一个迭代器，因此如果你想得到一个列表的话，就得像示例中那样使用List()
# filter()为已知的序列的每个元素调用给定的布尔函数，调用中，返回值为非零的元素将被添加至一个列表中