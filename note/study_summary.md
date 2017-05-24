## 在接收raw_input方法后，判断接收到的字符串是否为数字
例如：  
str = raw_input("please input the number:")  
if str.isdigit():  
为True表示输入的所有字符都是数字，否则，不是全部为数字  
str为字符串  
str.isalnum() 所有字符都是数字或者字母  
str.isalpha() 所有字符都是字母  
str.isdigit() 所有字符都是数字  
str.islower() 所有字符都是小写  
str.isupper() 所有字符都是大写  
str.istitle() 所有单词都是首字母大写，像标题  
str.isspace() 所有字符都是空白字符、\t、\n、\r  

上述的主要是针对整型的数字，但是对于浮点数来说就不适用了，那么浮点数怎么判断呢，一直在纠结这个问题，为什么非要区分整型和浮点数呢，既然都是参与运算的，全部适用浮点数不是一样吗，在得到结果后，直接转换为int型不是一样吗，为什么非要纠结在前期去判断是否整型或者浮点数呢，有了这样的思路，下面就好做了，例如：  
我们可以通过异常来判断，异常语法如下：  
try:  
    {statements}  
exception: {Exception Objects}  
    {statements}  

str = raw_input("please input the number:")  
try:  
    f = float(str)  
exception ValueError:  
    print("输入的不是数字！")  

还有一种纯粹判断是否为浮点数的方法，使用正则表达式：
1. 引用re正则模块  
import re  
float_number = str(input("Please input the number:"))  
2. 调用正则  
value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')  
result = value.match(float_number)  
if result:  
    print "Number is a float."  
else:  
    print "Number is not a float."  

2. 关于这个正则表达式，解释一下：  
^[-+]?[0-9]+\.[0-9]+$  
^表示以这个字符开头，也就是以[-+]开头，[-+]表示字符-或者+之一，
?表示0个或1个，也就是说符号是可选的。
同理[0-9]表示0到9的一个数字，+表示1个或多个，也就是整数部分。
\.表示的是小数点，\是转义字符因为.是特殊符号（匹配任意单个除\r\n之外的字符），
所以需要转义。
小数部分同理，$表示字符串以此结尾。

## Atom中的快捷键
| 快捷键 | 说明 |  
| ----- |-----|
|shift + cmd + p	| 命令版(可以看到所有快捷键)|
|alt + shift + s	|查看文件相关语言的代码块(snippet)
|cmd + f	|搜索当前文件
|cmd+shift+f	|搜索整个项目
|alt + cmd + [	|代码折叠, 我不喜欢用
|alt + cmd + ]	|代码展开
|cmd + /	|快速注释当前行
|cmd + [	|代码左缩进
|cmd + ]	|代码右缩进
|cmd + b	|快速跳转打开的文件

|光标移动快捷键	|说明|
|-----------|------|
|alt+B或alt+left	|光标按单词左移
|alt+F或alt+right	|光标按单词右移
|cmd+right或ctrl+e	|光标移动到行最右最后一个非空字符
|cmd+left或ctrl+a	|光标移动到行最左第一个非空字符
|cmd + up|	光标移动到文件头
|cmd + down	|贯标移动到文件尾
|ctrl + g	|行跳转, 语法为行号:列号
|cmd + r	|按当前文件方法跳转
|cmd + t	|全项目模糊查找关键字并跳转
|ctrl + m	|按照括号匹配跳转
书签功能: 通过cmd + F2给某一行设置书签, 书签的标志出现在行号右侧, 通过F2进行书签跳转. 此功能超赞

|选择和编辑快捷键	|说明|
|-|-|
|ctrl+shift+p	|向上选中行
|ctrl+shift+n	|向下选中行
|cmd + a	|选中整个文本
|cmd + l	|选中整行
|cmd + d	|多重选中, 用过sublime的都很熟悉
|ctrl+shit+k	|删除整行
|cmd + delete	|删除光标到行首
|alt + delete	|按单词删除
