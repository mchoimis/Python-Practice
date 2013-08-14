name = raw_input("Please enter your name.\n")
print 'How are you, ', name, '.\n'

age = input("What is your age?\n")
if int(age) >= 24:
    print 'Congratulations! You are qualified.\n'
else:
    print 'Sorry, you are not qualified.\n'
    
tel = raw_input("What is your phone number?\n")
while len(tel) != 10:
    print 'Please enter with 10 digits.'
    tel = raw_input("Again, what is your phone number?\n")
if len(tel) == 10:
    print 'Your number is ', tel, '.\n'
ask = raw_input("Can I call you at this number? (Y or N)\n")
if ask == 'yes':
    print "Thanks for your input.\n"
elif ask == 'Yes':
    print "Thanks for your input.\n"
else:
    print "Thanks, come again.\n"

