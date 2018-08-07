from sys import argv #Imports argument

script, input_file = argv #Assigns argv to script, input_file in order.

def print_all(f): #Prints all contents of a file.
    print f.read()

def rewind(f): #Seeks line 0 in the file.
    f.seek(0)

def print_a_line(line_count, f): #Print line_count and file's read line.
    print line_count, f.readline()
    

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Let's print three lines: "

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line - 1
print_a_line(current_line, current_file)