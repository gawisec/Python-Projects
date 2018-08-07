from sys import argv #Import argv library

script, filename = argv #Argument for script and filename

txt = open(filename) #Look and open for a file name.

print "Here's your file %r:" % filename #Prints string line, + its name. Taken from the argument
print txt.read() #Reads the text of file name.


print "Type the filename again: "
file_again = raw_input("> ") #Reads file name.
txt_again = open(file_again) #Opens file again and parses it to txt_again as a file object.

print txt_again.read() #Read's stored variable of txt_again

txt.close()
txt_again.close()