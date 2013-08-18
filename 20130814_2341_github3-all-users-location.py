# The github3 library supports iteration over all users.
# http://stackoverflow.com/questions/17128654/to-get-all-github-users-details


import github3

for user in github3.iter_all_users():
    user.refresh()
    print user.location

"""
For requests using Basic Authentication or OAuth, ~ 5,000 requests per hour.
For unauthenticated requests, ~ 60 requests per hour.

http://developer.github.com/v3/#rate-limiting
"""
