""" Here I try to solve the same problem as in 20130813_2322_len-int.py
but in different ways now that I learned 'while' statements. """

def function1():
    print "Thanks for your input."
def function2():
    print "Thanks for your input!"
def function3():
    print "Thanks, we'll call you."
def error_function():
    print "Please provide appropriate answer."

# Asking names with 4-8 letters
def ask1():
    while 1:
        name = raw_input("Choose your username.: ")
        if len(name) < 4:
            print "Can you think of something longer?"
        elif len(name) > 8:
            print "Our system doesn't hold that much."
        else:
            print 'Welcome, ' + name + '!\n'
            break

# Asking age in numbers - HALF WORKING
""" when entering strings, it returns an error message
because it's using input() not raw_input() function
so I'm not being able to contrict the input to numbers
also, I'm not limiting the range of the input, e.g., 100000 is possible
"""
# Don't forget parenthesis e.g., error_function() not error_function
# Don't be confused when prompting a question, input is object, not command

def ask2():
    while 1:
        age = input("How old are you?: ")
        if int(age) <= 0:
            error_function()
        elif int(age) > 100:
            error_function()
        elif int(age) < 14:
            print 'Grow up, kiddo.'
            break
        else:
            print 'You are fine.'
            break
                    
# Asking tel in 10 digits
def ask3():
    while 1:
        tel = input("What is your phone number?: ")
        if len(str(tel)) == 10:
            print "Your phone number is " + str(tel) + "."
            break        
        else:
            error_function()

# Asking to choose input and respond differently
def ask4():
    mapper = {'y':function1, 'Y':function2, 'yes':function3}
    while 1:
        code = raw_input('Is is ok to call you? (y / n): ')
        if code == 'n':
            break
        func = mapper.get(code, error_function)
        func()
        if mapper.get(code):
            break

def ask():
    ask1()
    print '-' * 10 + "ask1() name" + '-' * 10
    ask2()
    print '-' * 10 + "ask2() age" + '-' * 10
    ask3()
    print '-' * 10 + "ask3() tel" + '-' * 10
    ask4()
    print '-' * 10 + "ask4() ok to contact" + '-' * 10

if __name__ == '__main__':
    ask()
