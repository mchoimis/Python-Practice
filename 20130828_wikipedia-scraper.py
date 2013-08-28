from bs4 import  BeautifulSoup
import urllib2
import re
import nltk
import json


#get source code of page (function used later)
def fetchsource(url):
    source = urllib2.urlopen(url).read()
    return source

if __name__=='__main__':
    #url = "http://en.wikipedia.org/w/index.php?action=raw&title=Tom_Cruise" #works
    url="http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xml&&titles=Tom_Cruise" #works
    print url
    source = fetchsource(url)
    soup = BeautifulSoup(source)
    print soup.prettify()
