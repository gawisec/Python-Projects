def while_loop(i, x):
#    i = 0 #Declare integer variable as 'i'
#    x = 0
    numbers = [] #Declare list as 'numbers' 

    while i < x: #Conditional statement, run until condition is true.
        print "At the top i is %d" % i #Print i as decimal value.
        numbers.append(i) #Append value to 'numbers' list.

        i = i + 1 #Increment i (index)
        #similar to (for i=0, i++, i<6)
        print "Numbers now: ", numbers #print list.

        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num
        
    return i

while_loop(1, 11)