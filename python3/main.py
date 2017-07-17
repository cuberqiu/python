
# import ex3_list
from datetime import datetime

x = 100
nagetive = True

x = x +10 if not nagetive else x-10

print(x)

str1 = "${20170713}(-1,1)000000"
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
for i in range(len(str1)):
    if str1[i] == '{':
        count1 = i

    if str1[i] == '}':
        count2 = i

    if str1[i] == '(':
        count3 = i

    if str1[i] == ',':
        count4 = i

    if str1[i] == ')':
        count5 = i

print(count1,count2,count3,count4,count5)
num1 = str1[count1+1:count2]
print(num1)

str1 = "201703"

str1 = str1[:4]+'-'+str1[4:]
print(str1)




if __name__ == '__main__':
    str1 = "2017-01-01 12:00:00"
    str2 = "2017-0s-01 12:00:00"

    print(str1 > str2)
    tmp = str()

    for num in str1:
        if num.isdigit():
            tmp += num
    print(tmp)
    num = '1s'
    print(len(num))
    print(num[0].isnumeric())
    x = int(num[0])
    print(type(x),x)
    print("This is main")

    dep = "-1"
    print(dep.isdigit())