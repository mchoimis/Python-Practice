/*
	Written by FourwingsY
	Written at 2013. 12. 12.
	version 0.3
*/


function getHtmlDoc(_url) {
	var htmlString = null;

	$.ajax({
	    url: _url,
	    async : false,
	    type: 'GET',
	    success: function(result) {
	        htmlString = result;
	    }
	})

	var htmlDoc = document.createElement('html');
	htmlDoc.innerHTML = htmlString;
	return htmlDoc
}

function getText(element) {
    var text= [];

    for (var i= 0, n= element.childNodes.length; i<n; i++) {
        var child= element.childNodes[i];
        if (child.nodeType===1 && child.tagName.toLowerCase()!=='script')
			text = text.concat(getText(child));
        else if (child.nodeType===3 && child.textContent.replace(/\s|\n|\t/g,'') !== '')
			text = text.concat(child.data );
    }
    return text;
}

function parseUserName(title) {

	var name = getText(title)[0].split('\'s')[0]
	return {'name':name}
}

function parseUserStat(user_stats) {

	results = new Object()
	anchors = user_stats.getElementsByTagName("a")

	for (var i = 0; i < anchors.length; i++) {
		each = anchors[i];
		// 96 friends
		// 74 reviews
		// etc . . .
		stat = getText(each)[0].split(' ')

		if (stat[2] == 'Friends' || stat[2] == 'Friend') {
			results['friends_num'] = stat[1];
			continue;
		}
		if (stat[2] == 'Reviews' || stat[2] == 'Review') {
			results['reviews_num'] = stat[1]
			continue
		}
		if (stat[2] == 'Firsts' || stat[2] == 'First') {
			results['firsts_num'] = stat[1]
			continue
		}
	}
	return results
}

function parseEliteBagdes(elite_badges) {

	if (elite_badges == null)
		return new Object()

	elite_years = []
	anchors = elite_badges.getElementsByTagName('a')
	for (var i = 0; i < anchors.length; i++) {
		badge = anchors[i];
		// elite 2013
		title = badge.getAttribute("title")
		year = title.split(' ')[1]
		elite_years.push(year)
	}
	return {'elite':elite_years}
}

function parseReviewVotes(review_votes) {

	if (review_votes == null)
		return new Object()

	votes = getText(review_votes)[1].split(' ')
	// votes : 	[0] [1]64 [2]Useful, [3]13 [4]Funny,
	// 			[5]and [6]20 [7]Cool
	return {'votes':{'useful':votes[1], 'funny':votes[3], 'cool':votes[6]}}
}

function parseComplements(complements) {

	if (complements == null)
		return new Object()

	comp_total = 0
	comp_list = getText(complements)
	comp_list.splice(0,1)

	for (var i = 0; i < comp_list.length; i++) {
		comp_num = comp_list[i];
		comp_total += parseInt(comp_num)
	}
	return {'complements':comp_total.toString()}
}

function parseUserProfile(user_profile) {

	profile = getText(user_profile)

	return {'location':profile[1], 'since':profile[3]}
}

function parseUserPage(userid) {
	
	var PRE_URL = "http://www.yelp.com/user_details?userid="
	var url = PRE_URL + userid
	
	var htmlDoc = getHtmlDoc(url)
	var user_info = new Object()

	// case of closed user
	if (htmlDoc.querySelector('#inactive_user') != null) {
		user_info['userid'] = userid
		// user_info['name'] = "closed"
		user_info['since'] = "closed"
		user_info['location'] = "closed"

		return user_info
	}
	
	// stat and profile is always shown but others are not.
	var title = htmlDoc.querySelector('title')
	var user_stats = htmlDoc.querySelector('#user_stats')
	var elite_badges = htmlDoc.querySelector('#elite-badges')
	var review_votes = htmlDoc.querySelector('#review_votes')
	var complements = htmlDoc.querySelector('#userComplimentIcons')
	var user_profile = htmlDoc.querySelector('#profile_questions')
	
	// COLLECT USER INFO
	user_info['userid'] = userid
	jQuery.extend( user_info, parseUserName(title) )
	jQuery.extend( user_info, parseUserStat(user_stats) )
	jQuery.extend( user_info, parseEliteBagdes(elite_badges) )
	jQuery.extend( user_info, parseReviewVotes(review_votes) )
	jQuery.extend( user_info, parseComplements(complements) )
	jQuery.extend( user_info, parseUserProfile(user_profile) )
	return user_info
}


function parseFriend(friend) {
	var result = new Object()

	var name_tag = friend.querySelector("li.user-name")
	var location_tag = friend.querySelector("li.user-location")

	var name_anchor = name_tag.getElementsByTagName("a")[0]
	var user_url = name_anchor.getAttribute('href')
	var user_yelpid = user_url.split("=")[1];
	result['userid'] = user_yelpid

	var user_name = getText(name_anchor)[0]
	result['name'] = user_name

	var user_location = getText(location_tag)[0]
	result['location'] = user_location

	return result
}


function parseFriendPage(yelpid, start) {
	var PRE_URL = "http://www.yelp.com/user_details_friends?sort=first_name&userid="
	var POST_URL = "&start="
	var url = PRE_URL + yelpid + POST_URL + start
	
	var htmlDoc = getHtmlDoc(url)
	var friend_list = []

	// case of closed user
	if (htmlDoc.querySelector("#inactive_user") != null)
		return friend_list

	// GET FRIENDS NUMBER
	friends_num_dom = htmlDoc.querySelector("td.range-of-total")
	if (friends_num_dom == null) {
		return friend_list
	}
	friends_num = getText(friends_num_dom)[0].split(' ')[4]

	// PARSE FRIENDS
	friends = htmlDoc.querySelectorAll("div.friend_box")
	for (var i = 0; i < friends.length; i++) {
		friend = friends[i]
		friend_info = parseFriend(friend)
		friend_list.push(friend_info)
	}
	
	if (parseInt(friends_num) > (start + 100)) {
		post_list = parseFriendPage(yelpid, start + 100)
		friend_list = friend_list.concat(post_list)
	}

	return friend_list
}