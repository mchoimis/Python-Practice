# using stackpy in documentation // NOT WORKING

"""
Each of these methods operates on a single site at a time,
identified by the ::site:: parameter.
This parameter can be the full domain name (ie. "stackoverflow.com"),
or a short form identified by ::api_site_parameter:: on the site object.
"""

from stackpy import API, StackOverflow

# Print the names of all Stack Exchange sites
for stackoverflow.com in API.sites:
    print site['name']

# Grab the first question on Stack Overflow
print Site('stackoverflow').questions[0].title
