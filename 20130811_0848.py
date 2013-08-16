# Asking names with 4-8 letters

name = raw_input("Choose your username.\n")
if len(name) > 4:
    print 'How are you, ', name, '.\n'
elif len(name) 


# int()

age = input("What is your age?\n")
if int(age) >= 24:
    print 'Congratulations! You are qualified.\n'
else:
    print 'Sorry, you are not qualified.\n'
    

#len() returns the number of digits or letters of an object as integer
#len() doesn't take numbers as arguments?


tel = raw_input("What is your phone number?\n")
while len(tel) != 10:
    print 'Please enter with 10 digits.'
    tel = raw_input("Again, what is your phone number?\n")
if len(tel) == 10:          
    print 'Your number is ', tel, '.\n'
    
ask = raw_input("Can I call you at this number? (Y or N)\n")
if ask == 'y':
    print "Thanks for your input.\n"
elif ask == 'Y':
    print "Thanks for your input.\n"
else:
    print "Thanks, come again.\n"

