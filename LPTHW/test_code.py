from random import randint

code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
guess = int(input("[keypad]>"))
guesses = 1

while guess != code and guesses < 10:
    print "BUZZ!"
    guesses = guesses + 1
    print guesses
    print code
    guess = int(input("[keypad]>"))