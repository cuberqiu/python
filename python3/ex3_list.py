# coding:utf-8

# 列表的起始索引是从0开始的
lst = ['Google', 'Baidu', 'Tencent', 1998, 2000]

print(lst)

# 删除列表中的元素
del lst[3]
print(lst)

# 列表长度
lst_length = len(lst)

# 列表相加
lst = lst + [1, 2, 3]
print(lst)

# 某一元素是否在列表中
in_lst = 3 in lst

# # Python中包含以下函数：
# # 返回列表中元素最大值
# max(lst)
#
# # 返回列表中元素最小值
# min(lst)

lst = [1, 2, 3]

add = False
lst.extend([4, 5]) if add else None
print(lst)
