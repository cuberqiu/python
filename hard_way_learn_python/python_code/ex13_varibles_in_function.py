
# variables in function
def assign(x):
    print "origin x is :%r" %x
    x=10

# x is an unmutable argument
x=100
# After call assign(x),it wouldn't change the x's origin value
assign(x)
# Result: 100
print x

# define a function with two arguments
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(10,100)

print "Or, we can use variables from our scripts:"
amount_of_cheese = 11
amount_of_crackers = 22
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can do math inside too:"
cheese_and_crackers(10+1,21+1)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+11,amount_of_crackers+11)
