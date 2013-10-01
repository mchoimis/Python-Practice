import os
import sys
import httplib2
from BeautifulSoup import BeautifulSoup

conn = httplib2.Http(".cache-las-vegas")
url = u"http://www.yelp.com"
page = conn.request(url + '/browse/reviews/picks?edition_id=sE3ge33huDcNJGW3V4obww&start=',"GET")

# page[1] contains the retrieved html.

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('rotd-las-vegas0.txt', 'w')
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

file = open('rotd-las-vegas1.txt', 'w')
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

file = open('rotd-las-vegas2.txt', 'w')
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

file = open('rotd-las-vegas3.txt', 'w')
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

file = open('rotd-las-vegas4.txt', 'w')
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

file = open('rotd-las-vegas5.txt', 'w')
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

file = open('rotd-las-vegas6.txt', 'w')
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

file = open('rotd-las-vegas7.txt', 'w')
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

file = open('rotd-las-vegas8.txt', 'w')
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

file = open('rotd-las-vegas9.txt', 'w')
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

file = open('rotd-las-vegas10.txt', 'w')
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

file = open('rotd-las-vegas11.txt', 'w')
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

file = open('rotd-las-vegas12.txt', 'w')
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

file = open('rotd-las-vegas13.txt', 'w')
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

file = open('rotd-las-vegas14.txt', 'w')
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

file = open('rotd-las-vegas15.txt', 'w')
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

file = open('rotd-las-vegas16.txt', 'w')
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

file = open('rotd-las-vegas17.txt', 'w')
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

file = open('rotd-las-vegas18.txt', 'w')
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

file = open('rotd-las-vegas19.txt', 'w')
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

file = open('rotd-las-vegas20.txt', 'w')
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

file = open('rotd-las-vegas21.txt', 'w')
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

file = open('rotd-las-vegas22.txt', 'w')
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

file = open('rotd-las-vegas23.txt', 'w')
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

file = open('rotd-las-vegas24.txt', 'w')
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

file = open('rotd-las-vegas25.txt', 'w')
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

file = open('rotd-las-vegas26.txt', 'w')
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

file = open('rotd-las-vegas27.txt', 'w')
file.write(str(user))
file.close()
