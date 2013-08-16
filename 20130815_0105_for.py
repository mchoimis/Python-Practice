#1.6.2 for: statement, p. 33

""" The for: statment enables us to iterate over collections.
It enables us to repeat a set of lines of code one for each item in a collection.
Collections are things like strings (arrays of chracters), lists, tuples, and
dictionaries.
"""

collection = [111, 222, 333]
for item in collection:
    print 'item:', item


"""
Iterate over the keys or values in a dictionary with "aDict.keys()" and
"aDict.values()". Here is an example:
"""

aDict = {'cat': 'furry and cute', 'dog': 'friendly and smart'}
aDict.keys()
aDict.values()

for key in aDict.keys():
    print 'A %s is %s.' % (key, aDict[key])
    print len('A %s is %s.' % (key, aDict[key])) * '~'

# A dictionary itself is an iterator for its keys (which is the same).

for key in aDict:
    print 'A %s is %s.' % (key, aDict[key])
    print len('A %s is %s.' % (key, aDict[key])) * '*'
    print 'ho... note that a dog appears ahead of a cat\n'


# Also, a file is an iterator over the lines in the ile.

infile = file('infilename.txt', 'r')
for line in infile:
    print line,
    print '---- printed lines horizontally ----'

infile.close()

# built-in iterator, iter() is a built-in function
def test():
    anIter = iter([11, 22, 33])
    for item in anIter:
        print 'Here is what we have: ', item

test()

# you build your own iterator
def t(collection):
    icollection = iter(collection)
    for item in icollection:
        yield '||%s||' % item

def test():
    collection = [111, 222, 333, ]
    for x in t(collection):
        print x

test()

print 'defined test() again and it does not crash???'

