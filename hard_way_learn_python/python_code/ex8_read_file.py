#coding:utf-8
#这样做的原因是：如果写死要打开的文件，并不具有普实性
#因此，这些信息应该是用户输入的才对
from sys import argv

#script name(the python code) and file name(the file u will open)
script,file_name = argv

# open file use open command, it returns a file object
txt = open(file_name)

print "Here's your file %r: " %file_name
# read the file
# read the rest contents ,and will reach the end of the file
print txt.read()
# close the file opened
txt.close()

print "Type the filename again: "
# raw_input takes a parameter and returns a value you can set to your own
# varibles, and user the parameter to prompt the user input
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
