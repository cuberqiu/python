#coding:utf-8
#这样做的原因是：如果写死要打开的文件，并不具有普实性
#因此，这些信息应该是用户输入的才对
#from sys import argv

#script name(the python code) and file name(the file u will open)
#script,file_name = argv

script = "ex9_read_write_file.py"
file_name = "/home/wsn/Documents/python/hard_way_learn_python/file/write.txt"

# open file use open command, it returns a file object
txt = open(file_name,'r+w')

print "Here's your file %r: " %file_name

# read the file
for line in txt:
    print line,
# write contents to file
txt.write("I am cuber.\n")


# To write something other than a string,
# it needs to be converted to a string first:
value = "My age is ",24,"\n"
s = str(value)
txt.write(s+"\n")


# close the file opened
txt.close()
