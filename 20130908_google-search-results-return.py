# -*- coding: cp949 -*-
"""
http://coreapython.hosting.paran.com/dive/chap12.html
"""

from SOAPpy import WSDL

# you need to configure two values below;
# Refer to http://www.google.com/apis/
WSDLFILE = '/path/to/copy/of/GoogleSearch.wsdl'
APIKEY = 'YOUR_GOOGLE_API_KEY'

_server = WSDL.Proxy(WSDLFILE)
def search(q):
    """Search google and return the list that goes like {title, link, description}."""
    results = _server.doGoogleSearch(
        APIKEY, q, 0, 10, False, "", False, "", "utf-8", "utf-8")
    return [{"title": r.title.encode("utf-8"),
             "link": r.URL.encode("utf-8"),
             "description": r.snippet.encode("utf-8")}
            for r in results.resultElements]

if __name__ == '__main__':
    import sys
    for r in search(sys.argv[1])[:5]:
        print r['title']
        print r['link']
        print r['description']
        print

# I got an error message: No module named fpconst
# The Google Web Search API has been officially deprecated as of November 1, 2010.

