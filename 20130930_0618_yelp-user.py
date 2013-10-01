import os
import httplib2
from BeautifulSoup import BeautifulSoup

userid = "AF2wygvqImI9gbFijr13rw"

conn = httplib2.Http(".yelpcache")
url = "http://www.yelp.com/user_details?userid=" + userid
page = conn.request(url,"GET")

# page[1] contains the retrieved html.

soup = BeautifulSoup(page[1])
NoReviews = soup.findAll('p','formNote')
biz = soup.findAll('div','biz_info')
address = soup.findAll('address','smaller')
category = soup.findAll('p','smaller nobtm')
rating = soup.findAll('div','rating')
comment = soup.findAll('div class','review_comment')

user = zip(NoReviews,biz,address,category,rating,comment)

file = open('userid=AF2wygvqImI9gbFijr13rw.txt', 'w')
file.write(str(user))
# There was an error: "expected a buffer object" so I treated it as string. Then it worked.

file.close()

