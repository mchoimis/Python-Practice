# Writing

outfile = open('tmp.txt', 'w')
outfile.write('This is line #1\n')
outfile.write('This is line #2\n')
outfile.close()

# Reading an entire file

infile = file('tmp.txt', 'r')
content = infile.read()
print content
infile.close()

# Reading a file one line at a time
infile = file('tmp.txt', 'r')
for line in infile:
    print '$', line
infile.close()
