ugly = 'ugly\t' * 25
print ugly
    
if len(ugly) > 125:
    print 'ugly is greater than 125'
elif len(ugly) == 125:
    print 'ugly is 125'
else:
    print 'ugly is less than 125'

ugly.replace('u', 'uu')

print '*' * 20
print ugly

if len(ugly) > 125:
    print 'ugly is greater than 125'
elif len(ugly) == 125:
    print 'ugly is 125'
else:
    print 'ugly is less than 125'
