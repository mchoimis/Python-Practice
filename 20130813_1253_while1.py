# Python 101, p. 32
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

def test():
    test1()
    print '-' * 20
    
if __name__ == '__main__':
    test()
