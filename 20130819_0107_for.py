# 1.6.2.1 The for: statement and unpacking (python 101 p.35)

""" If an iterator produces a sequence of lists or tuples, each of which
contatin the same (small) number of items, then you can do unpacking directly
in the header of the ||for:|| statement. Here is an example.
"""

collection = [('apple', 'red'), ('bananna', 'yello'), ('kiwi', 'green')]
for name, color in collection:
    print 'name: %s, color: %s' % (name, color, ) # why comma here?
    
    
a = [11, 22, 33]
b = [111, 222, 333]
for idx, value enumerate(a):
    b[idx] += value

print a
print b

# enumerate is not working in the .py file. it only works in the interactive shell

