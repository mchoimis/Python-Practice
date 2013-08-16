# Python 101, p. 32
""" There are two different ways to solve the same problem here.
See the difference btw test1 and test2.

Also, at the end of line, there's a function declaring global function.
This is only for this local block of codes. Not importing.
"""

def function1():
    print "Hi. I'm function1."
def function2():
    print "Hi. I'm function2."
def function3():
    print "Hi. I'm function3."
def error_function():
    print "Noooooooo.....Invalid option."

def test1():
    while 1:
        code = raw_input('Enter "one", "two", "three", or "quit": ')
        if code == 'quit':
            break
        if code == 'one':
            function1()
        elif code == 'two':
            function2()
        elif code == 'three':
            function3()
        else:
            error_function()

# Note get() function

def test2():
    mapper = {'one':function1, 'two':function2, 'three':function3}
    while 1:
        code = raw_input('Please enter "one", "two", "three", or "quit": ')
        if code == 'quit':
            break
        func = mapper.get(code, error_function)
        func()

def test():
    test1()
    print '-' * 10 + "buil-in function 'break' is enabled. ending test1" + '-' * 10
    test2()
    print '-' * 10 + "buil-in function 'break' is enabled. ending test2" + '-' * 10

if __name__ == '__main__':
    test()
