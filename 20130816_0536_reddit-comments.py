# -*- coding: cp949 -*-
# Reddit API

"""
http://www.pythonforbeginners.com/python-on-the-web/how-to-use-reddit-api-in-python/

In an earlier post "How to access various Web Services in Python", we described
how we can access services such as YouTube, Vimeo and Twitter via their API's. 

Note, there are a few Reddit Wrappers that you can use to interact with Reddit. 

A wrapper is an API client, that are commonly used to wrap the API into easy to
use functions by doing the API calls itself. 

That results in that the user of it can be less concerned with how the code
actually works. 

If you don't use a wrapper, you will have to access the Reddits API directly,
which is exactly what we will do in this post.

We have chosen to extract information from our own Reddit account. 
  
"""

from pprint import pprint
import requests
import json

r = requests.get(r'http://www.reddit.com/user/spilcm/comments/.json')
r.text
# Now, we have a Response object called "r".
# We can get all the information we need from this object.

data = r.json()
# The Requests module comes with a built-in JSON decoder,
# which we can use for with the JSON data.
# As you could see on the image above, the output that we get is not
# really what we want to display. 
# The question is, how do we extract useful data from it? 
# If we just want to look at the keys in the "r" object:
    
# print data.keys()

# This should give us the following output: [u'kind', u'data']
# These keys are very important to us.

# print data['data']['children'][0]
# Remember that an array is indexed from zero.

for child in data['data']['children']:
    print child['data']['id'], "\r\n", child['data']['author'], child['data']['body']
    print
