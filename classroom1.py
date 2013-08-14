grades = 100 + 95 + 76 + 35 + 94
test_num = 7

try:
    grade = grades / test_num
except:
    grade = 0

print "Your total score:"
print grades
print "Your numerical grade:"
print grade

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 65:
    letter = 'D'
else:
    letter = 'F'

print "Your letter grade:"
print letter

#This is calculated by integers?
    
