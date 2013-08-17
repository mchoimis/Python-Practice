"""
Py-StackExchange: An API wrapper for Python
http://stackapps.com/questions/198/py-stackexchange-an-api-wrapper-for-python
For more, https://github.com/lucjon/Py-StackExchange

"""

# scrolling list of questions NOT WORKING

import os
import stackexchange

def write_questions():
    "output a list of questions to txt"
    file = open('stack-py2.txt', 'w')
    so = stackexchange.StackOverflow()
    for q in so.questions(pagesize=50):
        output = q.title
        file.write(output + os.linesep) ## writing line by line
    file.close()

write_questions()

"""
error message

Traceback (most recent call last):
  File "C:\Users\Nicole\Documents\Python-Practice-local\20130816_0224_stack-py2-2.py", line 22, in <module>
    write_questions()
  File "C:\Users\Nicole\Documents\Python-Practice-local\20130816_0224_stack-py2-2.py", line 19, in write_questions
    file.write(output)
UnicodeEncodeError: 'ascii' codec can't encode character u'\u2018' in position 44: ordinal not in range(128)

"""
