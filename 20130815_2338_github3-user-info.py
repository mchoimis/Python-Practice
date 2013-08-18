from github3 import login

gh = login('mchoimis', password='password')

sigmavirus24 = gh.user()
# <User [sigmavirus24:Ian Cordasco]>

print(sigmavirus24.name)
# Ian Cordasco
print(sigmavirus24.login)
# sigmavirus24
print(sigmavirus24.followers)
# 4

for f in gh.iter_followers():
    print(str(f))

kennethreitz = gh.user('kennethreitz')
# <User [kennethreitz:Kenneth Reitz]>

print(kennethreitz.name)
print(kennethreitz.login)
print(kennethreitz.followers)

followers = [str(f) for f in gh.iter_followers('kennethreitz')]

print followers
