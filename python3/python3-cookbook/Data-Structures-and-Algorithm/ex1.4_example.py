# coding:utf-8

# 查找最大或最小的N个元素

# 问题：怎样从一个集合中获得最大或最小的N个元素列表？

# heapqd模块有两个函数nlargest()和nsmallest()可以完美解决问题

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 这两个函数都可以接受一个关键字参数，用于更复杂的数据结构之中：
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# 实现机制：先对集合进行堆排序，然后弹出
heap = list(nums)
heapq.heapify(heap)
print(heap)
# 返回并弹出堆的第一个元素heap[0]
heapq.heappop(heap)
print(heap)

# 当查找的元素个数比较少时，使用nlargest和nsmallest两个元素很合适，如果仅仅查找最大的一个或最小的一个用max和min会比较快
print(max(nums))
print(min(nums))

# 如果N的大小和集合的大小接近时，通常先排序这个集合然后再使用切片操作会更快一点
# 查找最大的9个元素：
print(sorted(nums)[-9:])
# 查找最小的9个元素：
print(sorted(nums)[:9])