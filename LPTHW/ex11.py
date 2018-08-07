print "How old are you?",
age = int(raw_input()) #Converts int instead of string

print "How tall are you?",
height = raw_input() #raw_input() function converts input to string
#Then stores it to the variable.

print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heady." % (age, height, weight)