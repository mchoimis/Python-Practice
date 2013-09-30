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

file = open('yelp0.txt', 'w')
file.write(str(user))
file.close()

import re
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp1.txt', 'w')
file.write(str(user))
file.close()

#
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

#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp3.txt', 'w')
file.write(str(user))
file.close()

#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp4.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp5.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp6.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp7.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp8.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp9.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp10.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp11.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp12.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp13.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp14.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp15.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp16.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp17.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp18.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp19.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp20.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp21.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp22.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp23.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp24.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp25.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp26.txt', 'w')
file.write(str(user))
file.close()
#
soup.find(text=re.compile(r'Next')).parent.get('href')
page = conn.request(url + (soup.find(text=re.compile(r'Next')).parent.get('href')),"GET")

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('yelp27.txt', 'w')
file.write(str(user))
file.close()
