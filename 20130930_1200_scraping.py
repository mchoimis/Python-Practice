"""
http://lethain.com/an-introduction-to-compassionate-screenscraping/
a very useful article
"""

import httplib2
from BeautifulSoup import BeautifulSoup
conn = httplib2.Http(".cache")
page = conn.request(u"http://news.ycombinator.com/","GET")
page[0]
# then it turns folloiwng results. It seems like it shows the info of this page.
{'status': '200', 'content-location': u'http://news.ycombinator.com/', 'transfer-encoding': 'chunked', 'keep-alive': 'timeout=3', 'connection': 'Keep-Alive', 'content-type': 'text/html; charset=utf-8'}

page[1]
# page[1] contains the retrieved html.

... 

soup = BeautifulSoup(page[1])
titles = soup.findAll('td','title') # extracting info in <'td' class = 'title'>
titles = [x for x in titles if x.findChildren()][:-1]
# The bit with titles is necessarily confusing.
# The titles css class is used for both the 'td' tags that contain the number of the item (for example 1. or 15.),
#and for the td tags that contain the 'a' tags with the title of the story and its link.
# However, we only want the later kind, so we filter out the 'td' tags without any children tags.

# We're also excluding the last result from that filtered list.
#because the last one contains the More link to view the next 30 results, and is not actually a story itself.


subtexts = soup.findAll('td','subtext')
stories = zip(titles,subtexts)
# Right now each story is a 2-tuple of Tag objects.
len(stories)
# then it turns 30 because Hackernews frontpage has 30 titles.
stories[0]
# then it turns following result (0 means first element in Stories)
(<td align="right" valign="top" class="title">1.</td>, <td class="subtext"><span id="score_272314">38 points</span> by <a href="user?id=yangyang42">yangyang42</a> 5 hours ago  | <a href="item?id=272314">8 comments</a></td>)
