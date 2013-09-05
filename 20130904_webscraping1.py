"""
http://stackoverflow.com/questions/2081586/web-scraping-with-python

I'd like to grab daily sunrise/sunset times from here.
Is it possible to scrape web content with Python?
what are the modules used? Is there any tutorial available?
"""
"""
We're solving the same problem as 20130904_webscraping2.py
"""
import urllib2
from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://www.timeanddate.com/worldclock/astronomy.html?n=198').read())

for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
    tds = row('td')
    print tds[0].string, tds[1].string, tds[2].string, tds[3].string
    # will print date and sunrise
    # Minjung added third [2] and fourth [3] strings.
