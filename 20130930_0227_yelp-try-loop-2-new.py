import os
import sys
import httplib2
from BeautifulSoup import BeautifulSoup

conn = httplib2.Http(".cache-Philadelphia-PA-20131007")
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