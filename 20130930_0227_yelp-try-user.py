import os
import sys
import httplib2
from BeautifulSoup import BeautifulSoup

conn = httplib2.Http(".cache")
url = u"http://www.yelp.com"
page = conn.request(url + '/browse/reviews/picks?edition_id=hJ2dg0kOHm31nGAH-7zP6A&start=',"GET")

# page[1] contains the retrieved html.

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp.txt', 'w')
file.write(str(user))
# There was an error: "expected a buffer object" so I treated it as string. Then it worked.

file.close()

import re
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp2.txt', 'w')
file.write(str(user))
file.close()



