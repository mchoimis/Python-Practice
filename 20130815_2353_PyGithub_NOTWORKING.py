#First create a Github instance:
from github import Github

g = Github("mchoimis", "password")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print repo.name
    repo.edit(public=True, has_issues=True, has_downloads=True)
