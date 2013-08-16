# 2.2.5 Extracting multiple items.
# You can extract multiple items with a single search.

import sys, re

pat = re.compile('aa([0-9]*)bb([0-0]*)cc')

while 1:
    line = raw_input('Enter a line ("q" to quit): ')
    if line == 'q':
        break
    mo = pat.search(line)
    if mo:
        value1, value2 = mo.group(1, 2)
        print 'value1: %s value2: %s' % (value1, value2)
    else:
        print 'no match'
        
