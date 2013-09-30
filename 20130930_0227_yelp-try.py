import os
import sys
import httplib2
from BeautifulSoup import BeautifulSoup
conn = httplib2.Http(".cache")
url = 
page = conn.request(u"http://www.yelp.com/browse/reviews/picks?edition_id=hJ2dg0kOHm31nGAH-7zP6A&start=","GET")

# page[1] contains the retrieved html.

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location,userstats)

file = open('yelp.txt', 'w')
file.write(str(user))
# There was an error: "expected a buffer object" so I treated it as string. Then it worked.

file.close()

import re
soup.find(text=re.compile(r'Next')).parent.get('href')


# and we need cleansing, merging output

"""
If all above crawl is done, you go to the next page,
'http://www.yelp.com/browse/reviews/picks?start=' %s

and keep crawling.

page = conn.request(u"http://www.yelp.com/browse/reviews/picks?edition_id=hJ2dg0kOHm31nGAH-7zP6A","GET")

<a id="pager_page_next" class="pager-page" accesskey="n" href="/browse/reviews/picks?start=90">Next</a>


till you reach ____.


"""
