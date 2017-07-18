# coding:utf-8

from enum import Enum

# python中使用类来创建枚举


class System(Enum):
    AF = 'AF'
    LZ = 'LZ'

if System.AF.value == 'AF':
    print(System.AF.value)
else:
    print("error")
