file_name = "/home/wsn/Documents/python/hard_way_learn_python/file/write.txt"
script = "ex10_write.py"

print "We're going to erase %r." %file_name
print "If you don't want that, hit CTRL-C to cancel."
print "If you do want that, hit Return."

#raw_input("?")

print "Opening file "
target = open(file_name,'r+w')

print target.read()

print "Truncating the file "
#target.seek(0)
target.truncate()

print "Now, I amd going to ask you for three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I am going to write these to the file"
target.write(line1+'\n')
target.write(line2+'\n')
target.write(line3+'\n')

print "print the lines"
target.seek(0)
print target.read()

print "close the file"
target.close()
