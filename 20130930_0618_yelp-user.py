import os
import httplib2
from BeautifulSoup import BeautifulSoup

userid = "AF2wygvqImI9gbFijr13rw"

conn = httplib2.Http(".cache")
url = "http://www.yelp.com/user_details?userid=AF2wygvqImI9gbFijr13rw"
page = conn.request(url,"GET")

# page[1] contains the retrieved html.

soup = BeautifulSoup(page[1])
reviews = soup.findAll('p','formNote')
biz = soup.findAll('div','biz_info')
address = soup.findAll('address','smaller')
category = soup.findAll('p','smaller nobtm')
rating = soup.findAll('div','rating')

user = zip(reviews,biz,address,category,rating)

file = open('AF2wygvqImI9gbFijr13rw.txt', 'w')
file.write(str(user))
# There was an error: "expected a buffer object" so I treated it as string. Then it worked.

file.close()

