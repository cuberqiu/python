
people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats!The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs +=5

if people >= dogs:
    print "people are greater than or equal to dogs."

if people <= dogs:
    print "people are less than or equal to dogs."

if people == dogs:
    print "people are dogs."

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Finem let's stay home then."

if people < cars and buses < cars:
    print "We go!"
else:
    print "Go!"

if people > cars or buses < cars:
    print "Nice!"
else:
    print "No"
