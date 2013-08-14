print "This is the grade calculator."

last = raw_input("Student's last name: ")
first = raw_input("Student's first name: ")

test1 = input("First test: ")
test2 = input("Second test: ")
test3 = input("Third test: ")

average = (test1 + test2 + test3) / 3

report = "{last}, {first}\n\
Test 1: {test1}\n\
Test 2: {test2}\n\
Test 3: {test3}\n\
===========\n\
Average: {average}"

print report.format(last=last, first=first, test1=test1, test2=test2, test3=test3, average=average)
