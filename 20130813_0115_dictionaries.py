# An interesting feature of string formatting is the ability to use dictionaries.
# to supply the values that are inserted.

names = {'tree': 'sycamore', 'flower':'poppy', 'herb': 'arugula'}

print 'See what happens in (tree): %(tree)s' % names
print 'See what happens in (flower): %(flower)s' % names
print 'See what happens in (herb): %(herb)s' % names
