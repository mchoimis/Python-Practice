import os
import sys
import httplib2
from BeautifulSoup import BeautifulSoup

conn = httplib2.Http(".cache-louisville-ky")
url = u"http://www.yelp.com"
page = conn.request(url + '/browse/reviews/picks?edition_id=jQEQQKOmCe0oTia-6F6Pyw&start=',"GET")

# page[1] contains the retrieved html.

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('rotd-louisville-ky0.txt', 'w')
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

file = open('rotd-louisville-ky1.txt', 'w')
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

file = open('rotd-louisville-ky2.txt', 'w')
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

file = open('rotd-louisville-ky3.txt', 'w')
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

file = open('rotd-louisville-ky4.txt', 'w')
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

file = open('rotd-louisville-ky5.txt', 'w')
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

file = open('rotd-louisville-ky6.txt', 'w')
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

file = open('rotd-louisville-ky7.txt', 'w')
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

file = open('rotd-louisville-ky8.txt', 'w')
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

file = open('rotd-louisville-ky9.txt', 'w')
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

file = open('rotd-louisville-ky10.txt', 'w')
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

file = open('rotd-louisville-ky11.txt', 'w')
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

file = open('rotd-louisville-ky12.txt', 'w')
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

file = open('rotd-louisville-ky13.txt', 'w')
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

file = open('rotd-louisville-ky14.txt', 'w')
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

file = open('rotd-louisville-ky15.txt', 'w')
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

file = open('rotd-louisville-ky16.txt', 'w')
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

file = open('rotd-louisville-ky17.txt', 'w')
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

file = open('rotd-louisville-ky18.txt', 'w')
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

file = open('rotd-louisville-ky19.txt', 'w')
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

file = open('rotd-louisville-ky20.txt', 'w')
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

file = open('rotd-louisville-ky21.txt', 'w')
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

file = open('rotd-louisville-ky22.txt', 'w')
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

file = open('rotd-louisville-ky23.txt', 'w')
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

file = open('rotd-louisville-ky24.txt', 'w')
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

file = open('rotd-louisville-ky25.txt', 'w')
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

file = open('rotd-louisville-ky26.txt', 'w')
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

file = open('rotd-louisville-ky27.txt', 'w')
file.write(str(user))
file.close()
