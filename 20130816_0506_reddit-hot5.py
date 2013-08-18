# PRAW: The Python Reddit Api Wrapper
# documentation https://praw.readthedocs.org/en/latest/

""" Here's a quick peek, getting the first 5 submissions
from the 'hot' section of the 'opensource' subreddit:
"""

import praw
r = praw.Reddit(user_agent='my_cool_application')
submissions = r.get_subreddit('opensource').get_hot()
for x in submissions:
    print x


## when putting get_hot() without limit, limit is 25
## because the first page shows 25 entries!!
## that means you can call more "hot" lists if you go to next page!!
## In the output results, the number each line is the number of votes
