import os
import sys
import httplib2
from BeautifulSoup import BeautifulSoup

conn = httplib2.Http(".cache-20131007")
url = u"http://www.yelp.com"
page = conn.request(url + '/browse/reviews/picks?edition_id=hJ2dg0kOHm31nGAH-7zP6A&start=',"GET") #Philly
page = conn.request(url + '/browse/reviews/picks?edition_id=9549vDBw7ab0cuc930BQ1g&start=',"GET") #Houston
page = conn.request(url + '/browse/reviews/picks?edition_id=sE3ge33huDcNJGW3V4obww&start=',"GET") #Las Vegas
page = conn.request(url + '/browse/reviews/picks?edition_id=jQEQQKOmCe0oTia-6F6Pyw&start=',"GET") #Loisville
page = conn.request(url + '/browse/reviews/picks?edition_id=c6HT44PKCaXqzN_BdgKPCw&start=',"GET") #San Fran
page = conn.request(url + '/browse/reviews/picks?edition_id=RU7bd3h2f6pBlf8BfAyxGQ&start=',"GET") #nyc manhattan
page = conn.request(url + '/browse/reviews/picks?edition_id=O0nmI3IrPyK_jhDK6spZUQ&start=',"GET") #st paul 

# page[1] contains the retrieved html.

soup = BeautifulSoup(page[1])
ROTD = soup.findAll('strong','i-wrap ig-wrap-common i-yellow-star-common-wrap')
userstats = soup.findAll('ul','user-stats')
userstats = [x for x in userstats if x.findChildren()][:-1]
name = soup.findAll('li','user-name')
location = soup.findAll('li','user-location')

user = zip(ROTD,name,location)