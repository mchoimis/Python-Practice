import requests
import json

response = requests.get('https://api.github.com/users/j00bar')
response = requests.get('https://api.github.com/users/mchoimis')
response.json
d = response.json()
d.keys()
response.json()

# prompting input....doesn't work
name = raw_input(d['name'])
followers = input(d['followers'])
following = input(d['following'])


# working well
if d['following'] == d['followers']:
    print 'You have the same following and followers.'
elif d['following'] >= d['followers']:
    print 'You have more folloinwg than followers.'
elif d['following'] <= d['followers']:
    print 'You have less following than followers.'
elif d['following'] == d['followers'] == 0:
    print 'You have no followers and following. Start following.'

# working well!!!
if len(str(d['following'])) == 1:
    print 'You have less than 10 following. Expand your network!'
else:
    print 'You have lots of freinds. Share the tips.'
    

# printing 
print 'How are you?', d['name']
print 'You work for', d['company']
print 'Your public repository is', d['public_repos']
print 'Can I email you at', d['email']
print 'You joined', d['created_at']

# conditional statement
if d['name'] == 'Joshua "jag" Ginsberg':
    print 'You are the one!'
else:
    print 'You are not the one.'
    
