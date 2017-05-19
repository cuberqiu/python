#从命令行传参数进去
from sys import argv

script,user_name = argv
#将提示符设置为变量prompt，这样据不需要每次用到raw_input时，重复输入
#提示用户的字符了。
prompt = '> '

print "Hi %s, I am the %s script." %(user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer =  raw_input(prompt)

print """
Alright, so you said %r about liking me. You live in %r.Not sure where that is.
And you have a %r computer. Nice.""" %(likes,lives,computer)
