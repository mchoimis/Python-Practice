# dictionaries of dictionaries? NOT WORKING
# This code is working. 

def function1():
    print "You put yes."
def function2():
    print "You put no."
def error_function():
    print "Please provide appropriate answer."

# Asking to choose input
def ask4():
    mapper = {'y':function1, 'Y': function1, 'n':function2}
    while 1:
        code = raw_input('Is is ok to call you? (y / n) To quit, press q: ')
        if code == 'q':
            break
        func = mapper.get(code, error_function)
        func()

ask4()
print '-' * 10 + "ask4() ok to contact" + '-' * 10
