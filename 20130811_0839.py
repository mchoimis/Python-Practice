ugly = 'ugly\n' * 25
print ugly
    
ugly.replace('u', 'uu')

if len(ugly) > 125:
    print 'ugly is greater than 125'
elif len(ugly) == 125:
    print 'ugly is 125'
else:
    print 'ugly is less than 125'
