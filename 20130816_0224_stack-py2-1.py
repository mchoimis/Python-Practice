"""
Py-StackExchange: An API wrapper for Python
http://stackapps.com/questions/198/py-stackexchange-an-api-wrapper-for-python
For more, https://github.com/lucjon/Py-StackExchange

"""

# Or how about a scrolling list of questions? Utterly incredulous, eh?

import stackexchange

so = stackexchange.StackOverflow()
for q in so.questions(pagesize=50):
    print q.title
