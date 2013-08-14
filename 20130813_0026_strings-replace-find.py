# string
state = raw_input('Where do you live?: ')
print 'I live in %s.' % state

## in the exporting issue tracker API to csv problem,

r = requests.get(ISSUES_FOR_REPO_URL, auth=AUTH)
csvfile = '%s-issues.csv' % (REPO.replace('/', '-'))
csvout = csv.writer(open(csvfile, 'wb'))

## open() built-in function creats a file.
## It takes as arguments (1) file name and (2) a mode.
## Commonly used modes are "r"(read), "w"(write), and "a"(append).
## Then, what is 'wb' here?
