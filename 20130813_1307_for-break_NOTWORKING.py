# for_break.py NOT WORKING
"""Count lines until a line that begins with a double #.
"""

import sys

outfile = open('infilename.txt', 'w')
outfile.write('#1\n')
outfile.write('#2\n')
outfile.write('##\n')
outfile.close()

def countLines(infilename):
    infile = file(infilename, 'r')
    count = 0
    for line in infile.readlines():
        line = line.strip()
        if line[:2] == '##':
            break
        count += 1
    return count

def usage():
    print 'Usage: python python_101_for_break.py <infilename.txt>'
    sys.exit(-1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    count = countLines(args[0])
    print 'count:', count

if __name__ == '__main__':
    main()
