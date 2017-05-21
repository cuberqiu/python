from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copying from %s to %s" %(from_file,to_file)

input = open(from_file,'r+w')
indata = input.read()

# len()function gets the length of the string that you pass to it
print "The input file is %d bytes long, and it's contens are :%s" %(len(indata),indata)

# exists(argv),it returns TRUE if a file exists,
# based on its name in a string as an argument.
print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("> ")

output = open(to_file,'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()
