import json

from socketpool import ConnectionPool
from restkit import Resource, BasicAuth, Connection, request

pool = ConnectionPool(factory=Connection)
serverurl="https://api.github.com"
 
# Add your username and password here, or prompt for them
auth=BasicAuth(user, password)
 
# Use your basic auth to request a token
# This is just an example from http://developer.github.com/v3/
authreqdata = { "scopes": [ "public_repo" ],
                "note": "admin script" }
resource = Resource('https://api.github.com/authorizations', 
                    pool=pool, filters=[auth])
response = resource.post(headers={ "Content-Type": "application/json" }, 
                         payload=json.dumps(authreqdata))
token = json.loads(response.body_string())['token']
 
"""
Once you have a token, you can pass that in the Authorization header
You can store this in a cache and throw away the user/password
This is just an example query.  See http://developer.github.com/v3/ 
for more about the url structure
"""
resource = Resource('https://api.github.com/user/repos', pool=pool)
headers = {'Content-Type' : 'application/json' }
headers['Authorization'] = 'token %s' % token
response = resource.get(headers = headers)
repos = json.loads(response.body_string())
