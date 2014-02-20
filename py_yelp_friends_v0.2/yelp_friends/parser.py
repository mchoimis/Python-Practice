"""

Written by FourwingsY
Written at 2013. 12. 6.
version 0.2

"""

# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
from time import sleep

"""
Table User
"""
def parseUserName(title) :
	name = title.get_text().split('\'s')[0]
	return {'name':name}

def parseUserStat(user_stats) :

	results = {}
	anchors = user_stats.find_all("a")
	for each in anchors :

		# 96 friends
		# 74 reviews
		# etc . . .
		stat = each.get_text().split()

		if stat[1] == 'Friends' or stat[1] == 'Friend' :
			results['friends_num'] = stat[0]
			continue
		if stat[1] == 'Reviews' or stat[1] == 'Review':
			results['reviews_num'] = stat[0]
			continue
		if stat[1] == 'Firsts' or stat[1] == 'First':
			results['firsts_num'] = stat[0]
			continue

	return results

def parseEliteBagdes(elite_badges) :

	if (elite_badges == None) :
		return {}

	elite_years = []
	anchors = elite_badges.find_all('a')
	for badge in anchors :
		# elite 2013
		title = badge['title']
		year = title.split()[1]
		elite_years.append(year)

	return {'elite':elite_years}

def parseReviewVotes(review_votes) :

	if (review_votes == None) :
		return {}

	votes = review_votes.get_text().split()
	# votes : 	[0]Review [1]votes: [2]64 [3]Useful, [4]13 [5]Funny,
	# 			[6]and [7]20 [8]Cool
	return {'votes':{'useful':votes[2], 'funny':votes[4], 'cool':votes[7]}}

def parseComplements(complements) :

	if (complements == None) :
		return {}

	comp_total = 0
	comp_list = complements.get_text().split()
	del comp_list[0]
	for comp_num in comp_list :
		comp_total += int(comp_num)

	return {'complements':str(comp_total)}

def parseUserProfile(user_profile) :

	profile = user_profile.get_text().split('\n')

	return {'location':profile[2], 'since':profile[4]}


def parseUserPage(userid) :
	PRE_URL = "http://www.yelp.com/user_details?userid="
	
	print "Downloading Page... " + userid
	url = PRE_URL + userid
	html_doc = urllib.urlopen(url).read()
	soup = BeautifulSoup(html_doc)
	user_info = {}

	# case of closed user
	if soup.find(id="inactive_user") != None :
		user_info['userid'] = userid
		user_info['name'] = "closed"
		user_info['since'] = "closed"
		user_info['location'] = "closed"
		return user_info

	# stat and profile is always shown but others are not.
	title = soup.find("title")
	user_stats = soup.find(id="user_stats")
	elite_badges = soup.find(id="elite-badges")
	review_votes = soup.find(id="review_votes")
	complements = soup.find(id="userComplimentIcons")
	user_profile = soup.find(id="profile_questions")

	# COLLECT USER INFO
	user_info['userid'] = userid
	user_info.update( parseUserName(title) )
	user_info.update( parseUserStat(user_stats) )
	user_info.update( parseEliteBagdes(elite_badges) )
	user_info.update( parseReviewVotes(review_votes) )
	user_info.update( parseComplements(complements) )
	user_info.update( parseUserProfile(user_profile) )

	return user_info

"""
Table Friend
"""
def parseFriend(friend) :

	result = {}
	name_tag = friend.find("li", {"class":"user-name"})
	location_tag = friend.find("li", {"class":"user-location"})

	user_url = name_tag.a.get('href')
	user_yelpid = user_url.split("=")[1];
	result.update({"userid":user_yelpid})

	user_name = name_tag.a.get_text()
	result.update({"name":user_name})

	user_location = location_tag.get_text()
	result.update({"location":user_location})

	return result

def parseFriendPage(yelpid, start) :
	PRE_URL = "http://www.yelp.com/user_details_friends?sort=first_name&userid="
	POST_URL = "&start="

	print "Downloading Friends... # " + str(start)
	url = PRE_URL + yelpid + POST_URL + str(start)
	html_doc = urllib.urlopen(url).read()
	soup = BeautifulSoup(html_doc)
	friend_list = []

	# case of closed user
	if soup.find(id="inactive_user") != None :
		return friend_list

	# GET FRIENDS NUMBER
	friends_num_dom = soup.findAll("td", {"class":"range-of-total"})[0]
	friends_num = friends_num_dom.span.get_text().split(' ')[4]
	# print "Total Number of Friends: " + friends_num

	# PARSE FRIENDS
	friends = soup.findAll("div", {"class":"friend_box"})
	for friend in friends :
		friend_info = parseFriend(friend)
		friend_list.append(friend_info)
	# print "number of friends parsed = " + str(len(friend_list))
	
	if (int(friends_num) > (start + 100)) :
		sleep(2)
		post_list = parseFriendPage(yelpid, start + 100)
		friend_list += post_list

	return friend_list

"""
Table Biz
"""
def parseHeader(biz_header) :
	# to remove white space, split and join.
	name_text = biz_header.find("h1").get_text().split()
	biz_name = ' '.join(name_text)

	rating = biz_header.find("meta")["content"]
	review_count = biz_header.find("span").get_text().split()[0]

	return {'name':biz_name, 'total_rating':rating, 'review_count':review_count}

def parseCategory(biz_category) :

	result = []
	categories = biz_category.find_all("span", {'class':'hidden'})
	
	# one biz can multiple 
	for category in categories :
		category_level = []
		for span in category.find_all("span") :
			if span.a == None :
				category_level.append(span.get_text())
		result.append(category_level)

	return {'category':result}

def parseAddress(biz_address) :
	address_tag = biz_address.find_all("span")
	address_words = []
	for span in address_tag :
		address_words.append(span.get_text())
	address = ' '.join(address_words)

	return {'address':address}

def parseBizPage(biz_url) :
	PRE_URL = "http://www.yelp.com/biz/"

	print "Downloading Page..."
	url = PRE_URL + biz_url
	html_doc = urllib.urlopen(url).read()
	soup = BeautifulSoup(html_doc)
	biz_info = {}

	biz_header = soup.find(id="bizInfoHeader")
	biz_category = soup.find(id="bizCategories")
	biz_address = soup.find("address")
	price_info = soup.find(id="price_tip")

	# COLLECT BIZ INFO
	biz_info['biz_url'] = biz_url
	biz_info.update( parseHeader(biz_header) )
	biz_info.update( parseCategory(biz_category) )
	biz_info.update( parseAddress(biz_address) )
	
	if (price_info != None) :
		price = price_info.get_text()
		biz_info['price'] = price

	return biz_info

"""
Table Review
"""
def parseReview(review) :
	result = {}
	review_biz = review.find("div", {"class":"biz_info"})
	review_meta = review.find("div", {"class":"review-meta"})
	review_text = review.find("div", {"class":"review_comment"})

	# REVIEW ABOUT
	biz_link = review_biz.h4.a
	biz_name = biz_link.get_text()
	biz_url = biz_link["href"].split("#")[0].split('/')
	result.update({"biz_url":biz_url[2]})

	# META DATA
	rating_title = review_meta.i["title"]
	rating = rating_title.split()[0]
	result.update({"rating":rating})

	post_date = review_meta.span.get_text().split()
	result.update({"post_date":post_date[-1]})

	# REVIEW TEXT
	review_encode = review_text.get_text().encode('utf-8')
	result.update({"review":review_encode})

	return result

def parseReviewPage(yelpid, start) :
	PRE_URL = "http://www.yelp.com/user_details_reviews_self?userid="
	POST_URL = "&rec_pagestart="

	print "Downloading Reviews... # " + str(start)
	url = PRE_URL + yelpid + POST_URL + str(start)
	html_doc = urllib.urlopen(url).read()
	soup = BeautifulSoup(html_doc)
	parsedReviews = []

	# GET REVIEW NUMBER
	reviews_num_dom = soup.findAll("td", {"class":"range-of-total"})
	reviews_num = reviews_num_dom[0].span.get_text().split(' ')[4]
	# print "Number of reviews: " + reviews_num

	# PARSE REVIEW
	reviews = soup.findAll("div", {"class":"review"})
	for review in reviews :
		parsedReview = parseReview(review)
		parsedReview['writerid'] = yelpid

		parsedReviews.append(parsedReview)

	if (int(reviews_num) > (start + 10)) :
		parseReviewPage(yelpid, start + 10)

	return parsedReviews