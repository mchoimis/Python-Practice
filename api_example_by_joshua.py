# in the windows command window (win tab -> cmd)

import requests
import json
response = requests.get('http://google.com/')
response.body
response.content

response = requests.get('http://graph.facebook.com/me')

response = requests.get('http://graph.facebook.com/me')
response.body
response.content
response.json()

d = response.json() #define?

d['error']
d['error']['message']
d['error']['code']

response = requests.get('https://api.github.com/users/j00bar')
response.status_code
d.keys()
d['bio']
d['company']
d['name']
