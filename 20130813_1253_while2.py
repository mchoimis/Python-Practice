# Python 101, p. 32, test2
def function1():
    print "Hi. I'm function1."
def function2():
    print "Hi. I'm function2."
def function3():
    print "Hi. I'm function3."
def error_function():
    print "Noooooooo.....Invalid option."


def test2():
    mapper = {'one':function1, 'two':function2, 'three':function3}
    while 1:
        code = raw_input('Please enter "one", "two", "three", or "quit": ')
        if code == 'quit':
            break
        func = mapper.get(code, error_function)
        func()

def test():
    print '-' * 20
    test2()

if __name__ == '__main__':
    test()
