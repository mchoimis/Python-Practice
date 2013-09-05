"""
http://stackoverflow.com/questions/2081586/web-scraping-with-python

I'd like to grab daily sunrise/sunset times from here.
Is it possible to scrape web content with Python?
what are the modules used? Is there any tutorial available?
"""
"""
We're solving the same problem as 20130904_webscraping1.py
"""
from webscraping import download, xpath
D = download.Download()

html = D.get('http://www.timeanddate.com/worldclock/astronomy.html?n=198')
for row in xpath.search(html, '//table[@class="spad"]/tbody/tr'):
    cols = xpath.search(row, '/td')
    print 'Date: %s | Sunrise: %s | Sunset: %s' % (cols [0], cols[1], cols[2])

#Minjung added the first column [0]
