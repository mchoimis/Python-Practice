"""

Written at 2013. 11. 30
version 0.1

"""

USER_NUM_TO_READ = 10
MAXIMUM_FRIENDS_NUM = 200
PRE_URL = "http://www.yelp.com/user_details_friends?userid="
POST_URL = "&start="

"""
basic library in python.
do not have to install.
get html document by url.
"""
import urllib

"""
Download from http://www.crummy.com/software/BeautifulSoup/
library for Parsing html.
"""
from bs4 import BeautifulSoup


def parseFriends(_url, start) :

	if (start >= MAXIMUM_FRIENDS_NUM) :
		return []

	print "Downloading Page #" + str(start) # + _url
	html_doc = urllib.urlopen(_url).read()
	soup = BeautifulSoup(html_doc)

	_friends = soup.find_all("div", "friend_box")
	_friend_list = []

	# ADD TO LIST
	print "Parsing Page #" + str(start) # + _url
	for friend in _friends :
		_name_tag = friend.find("li", "user-name")
		_user_fullURL = _name_tag.a.get('href').encode('utf-8')
		_user_url = _user_fullURL.split("=")[1];
		_user_name = _name_tag.a.string.encode('utf-8')
		_friend_list.append({'url':_user_url, 'name':_user_name})

	# GO TO NEXT PAGE
	friends_num_dom = soup.findAll("td", {"class":"range-of-total"})[0]
	friends_num = friends_num_dom.find("span").string.split(' ')[4]
	given_url = _url.split('=')[1].split('&')[0]

	if (int(friends_num) > (int(start) + 100)) :
		new_url = PRE_URL + given_url + POST_URL + str(start+100)
		_friend_list += parseFriends(new_url, start+100)

	return _friend_list

def init() :
	print "initializing \n"
	start_info = open('start_info.txt', 'r+')

	info = start_info.readline()
	user_url = info.split('=')[1]
	_url = "http://www.yelp.com/user_details?userid=" + user_url

	html_doc = urllib.urlopen(_url).read()
	soup = BeautifulSoup(html_doc)
	title = soup.find("title").string
	user_name = title.split("'")[0]

	global file_user
	file_user.seek(0)
	file_user.write("1 -1 \n")
	file_user.write("0 " + user_url + " " + user_name)

	start_info.close()

# SET DATABASE FILE
file_user = open('users.txt', 'w+')
file_relation = open('relations.txt', 'w+')

# CHECK FILE_USER IS EMPTY
# first_line = file_user.readline()
# if first_line == "" :
init()
file_user.seek(0)

# READ USER DATA FROM FILE
user_list = {}
user_meta = file_user.readline().split(" ")
user_num = int(user_meta[0])
user_toread = int(user_meta[1])
url2id = {}

for line in file_user :
	if line == '\n' :
		continue;
	user_data = line.split(" ")
	user_name = user_data[2] + " " + user_data[3]
	user_list.update({int(user_data[0]):{'url':user_data[1], 'name':user_name}})
	url2id.update({user_data[1]:user_data[0]})


# READ RELATION DATA FROM FILE
relation_list = []
rel_num = file_relation.readline()

for line in file_relation :
	relation_data = line.split(" ")
	relation_tuple = relation_data[0], relation_data[1][:-1]
	relation_list.append(relation_tuple)


# LOAD PAGE, PARSE
while (user_toread < USER_NUM_TO_READ) :
	# SET CURRENT USER
	current_user_id = user_toread + 1
	current_user = user_list[current_user_id]
	print "Access to user: " + current_user['name']

	start_url = current_user['url']
	url = PRE_URL + start_url + POST_URL + "0"

	# GET FRIENDS LIST
	friend_list = parseFriends(url, 0)
	for friend in friend_list :
		if friend['url'] in url2id.keys() :
			friend_id = url2id[friend['url']]
			relation_list.append((current_user_id, friend_id))
			continue;
		user = {user_num:friend}
		user_list.update(user)
		relation_list.append((current_user_id, user_num))
		user_num += 1

	user_toread += 1

	print "%dth user completed" % user_toread
	print "now, total: %d users are in the list" % user_num


print "Save the result"
# SAVE USER LIST
file_user.seek(0)
file_user.write(str(user_num) + ' ' + str(user_toread) + '\n')
for user in user_list.keys() :
	file_user.write(str(user) + ' ' + 
		user_list[user]['url'] + ' ' +
		user_list[user]['name'] + '\n')

# SAVE RELATION LIST
file_relation.seek(0)
for relation in relation_list :
	file_relation.write(str(relation[0]) + ' ' + str(relation[1]) + '\n')


file_user.close()
file_relation.close()
