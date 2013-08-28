# This is not working


import wikipedia

page = wikipedia.Page(wikipedia.getSite(), 'Tom_Cruise')

pageText = page.get()

print pageText
