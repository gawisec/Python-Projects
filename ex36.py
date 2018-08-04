print "Welcome to the metro station!"
print "You have encountered a soil rat."
print "What will you do? "

user_option = raw_input("> ")

if user_option == "1":
    print "Retreat to the metro!"
    metro_station()
elif user_option == "2":
    print"Retreat to the wilderness!"

def metro_station():
    print "You are in the metro station."


def landscape():
    print "You are outside the landscape."