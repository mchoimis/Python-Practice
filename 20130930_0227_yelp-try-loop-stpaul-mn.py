import os
import sys
import httplib2
from BeautifulSoup import BeautifulSoup

conn = httplib2.Http(".cache-stpaul-mn")
url = u"http://www.yelp.com"
page = conn.request(url + '/browse/reviews/picks?edition_id=O0nmI3IrPyK_jhDK6spZUQ&start=',"GET")

# page[1] contains the retrieved html.

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)

file = open('rotd-stpaul-mn0.txt', 'w')
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

file = open('rotd-stpaul-mn1.txt', 'w')
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

file = open('rotd-stpaul-mn2.txt', 'w')
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

file = open('rotd-stpaul-mn3.txt', 'w')
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

file = open('rotd-stpaul-mn4.txt', 'w')
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

file = open('rotd-stpaul-mn5.txt', 'w')
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

file = open('rotd-stpaul-mn6.txt', 'w')
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

file = open('rotd-stpaul-mn7.txt', 'w')
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

file = open('rotd-stpaul-mn8.txt', 'w')
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

file = open('rotd-stpaul-mn9.txt', 'w')
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

file = open('rotd-stpaul-mn10.txt', 'w')
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

file = open('rotd-stpaul-mn11.txt', 'w')
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

file = open('rotd-stpaul-mn12.txt', 'w')
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

file = open('rotd-stpaul-mn13.txt', 'w')
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

file = open('rotd-stpaul-mn14.txt', 'w')
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

file = open('rotd-stpaul-mn15.txt', 'w')
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

file = open('rotd-stpaul-mn16.txt', 'w')
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

file = open('rotd-stpaul-mn17.txt', 'w')
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

file = open('rotd-stpaul-mn18.txt', 'w')
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

file = open('rotd-stpaul-mn19.txt', 'w')
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

file = open('rotd-stpaul-mn20.txt', 'w')
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

file = open('rotd-stpaul-mn21.txt', 'w')
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

file = open('rotd-stpaul-mn22.txt', 'w')
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

file = open('rotd-stpaul-mn23.txt', 'w')
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

file = open('rotd-stpaul-mn24.txt', 'w')
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

file = open('rotd-stpaul-mn25.txt', 'w')
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

file = open('rotd-stpaul-mn26.txt', 'w')
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

file = open('rotd-stpaul-mn27.txt', 'w')
file.write(str(user))
file.close()
