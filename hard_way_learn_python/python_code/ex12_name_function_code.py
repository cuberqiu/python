# When you start to define a function , you need to consider:
"""
    1.Did you start your function definition with def?
    2.Does your function name have only characters and _(underscore)characters?
    3.Did you put an open parenthesis ( right after the funciton name?
    4.Did you put your arguments after the parenthesis ( serparated by commas?
    5.Did you make each argument unique(meaning no duplicated names)?
    6.Did you put a close parenthesis and a colon ): after the arguments?
    7.Did you indent all lines of code you want in the function four spaces?No more,no less.
    8.Did you "end" your fucntion by going back to writiing with no indent?
"""
# When you run a function,check these things
"""
    1.Did you call/use/run this function by typing its name?
    2.Did you put the ( character after the name to run it?
    3.Did you put the values you want into the parenthesis serparated by commas?
    4.Did you end the function call a ) character?
"""

# this one is like your scripts with argv
"""
 * tells python to take all the arguments to the function and then put them in
 args as a list.
"""
def print_two(*args):
    # interprete the arguments
    arg1,arg2 = args
    print "arg1: %r, arg2: %r" %(arg1,arg2)

# *arg is actually pointless, we can just do as following
def print_two_again(arg1,arg2):
    print "arg1: %r,arg2: %r" %(arg1,arg2)

# just take one argument
def print_one(arg):
    print "arg: %r" %arg

# takes no argument
def print_non():
    print "I get nonthing"

arg1 = "bobo"
arg2 = "cuber"
print_two(arg1,arg2)
print_two_again(arg1,arg2)
print_one(arg1)
print_non()