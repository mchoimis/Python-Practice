# This is not working

from bs4 import  BeautifulSoup
import urllib2
import re
import nltk
import json
import wikipedia

page = wikipedia.Page(wikipedia.getSite(), 'Tom_Cruise')

pageText = page.get()

print pageText
