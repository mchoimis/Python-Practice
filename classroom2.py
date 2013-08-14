print "This is the grade calculator."

last = raw_input("Student's last name: ")
first = raw_input("Student's first name: ")

tests = [] #First, give a blank list

test1 = input("First test: ")
tests.append(test1) #You add an item to the list named "tests" using .append.
test2 = input("Second test: ")
tests.append(test2)
test3 = input("Third test: ")
tests.append(test3)

average = (tests[0] + tests[1] + tests[2]) / len(tests) #indexing starts from 0

report = "{last}, {first}\n\
Test 1: {test1}\n\
Test 2: {test2}\n\
Test 3: {test3}\n\
===========\n\
Average: {average}" #Don't know why they used curly brackets {}?

print '\n'
print "Here is the student's report."
print report.format(last=last, first=first,
	test1=tests[0], test2=tests[1], test3=tests[2],
	average=average) #Don't know if the function report.format exists?
