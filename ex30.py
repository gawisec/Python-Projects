people = 30
cars = 40
buses = 15

if cars > people: #Run if condition is met.
    print "We should take the cars."
elif cars < people: #Run this if condition above is not met.
    print "We should not take the cars."
else: #Run if both conditions above are not met.
    print "We can't decide."

if buses > cars: #Run if condition is met.
    print "That's too many buses."
elif buses < cars: #Run if condition above is not met but meets this condition.
    print "Maybe we could take the buses."
else: #Run this if both conditions above is not met.
    print "We still can't decide."

if people > buses: #Run statement if people are greater than buses.
    print "Alright, let's just take the buses."
else: #If false, then run this statement.
    print "Fine, let's stay home then."