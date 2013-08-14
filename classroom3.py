print "This is the grade calculator." 

last = raw_input("Student's last name: ")
first = raw_input("Student's first name: ")

tests = []
test = 0                            #Why test = 0 ?

while True:
    test = input("Test grade: ")
    if test < 0:
        break
    tests.append(test)
    
total = 0                           #Why total = 0 ?
for test in tests:
    total = total + test
    
average = total / len(tests)        #Note the number of tests varies.

print "*" * 20
print "Student's name: ", first, last

num = 1
for test in tests:
    print "Test {num}: {grade}".format(num=num, grade=test)
    num = num + 1

print "Average: {average}".format(average=average) #Dont' know format...
