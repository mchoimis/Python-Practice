#First create a Github instance:
from github import Github

g = Github("mchoimis", "snu10338")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print repo.name
    repo.edit(has_wiki=False)
