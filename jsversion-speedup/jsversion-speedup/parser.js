/*
	Written by FourwingsY
	Written at 2013. 12. 30.
	version 0.4
*/


function getHtmlDoc(_url, callback) {
	var htmlString = null;
	callbackNum += 1;
	$.ajax({
		url: _url,
		type: 'GET',
		success: function(result) {
			htmlString = result;
			// remove script or img tag
			htmlString = htmlString.replace(/<script/g, "<sccc ")
			htmlString = htmlString.replace(/script>/g, "sccc>")
			htmlString = htmlString.replace(/<img/g, "<immmmm ")

			var htmlDoc = document.createElement('html');
			htmlDoc.innerHTML = htmlString;

			callback(htmlDoc);
		}
	})
}

function removeWhiteSpace(text) {
	var tempText = text.replace(/\s+/g, ' ');
	var length = tempText.length
	
	var startSpace = 0
	var endSpace = 0

	if (tempText[0] == ' ')
		var startSpace = 1
	if (tempText[length-1] == ' ')
		var endSpace = 1

	if (startSpace + endSpace > 0)
		tempText = tempText.slice(startSpace, length - endSpace)
	return tempText
}

function clearList(list) {
	var newList = []
	for (var i = 0; i < list.length; i++) {
		if (list[i] == "") 
			continue
		else newList.push(removeWhiteSpace(list[i]))
	}
	return newList
}
/*
	returns an Object about a User
*/
function parseAndInsertUserPage(db, userId) {
	var PRE_URL = "http://www.yelp.com/user_details?userid="
	var url = PRE_URL + userId
	var userInfo = new Object()

	getHtmlDoc(url, function(htmlDoc) {
		console.log(callbackNum);
		// case of closed user
		if (htmlDoc.querySelector('#inactive_user') != null) {
			userInfo['user_id'] = userId
			// userInfo['name'] = "closed"
			userInfo['since'] = "closed"
			callbackNum -= 1
			return userInfo
		}
		
		// stat and profile is always shown but others are not.
		var title = htmlDoc.querySelector('title')
		var userStats = htmlDoc.querySelector('#user_stats')
		var eliteBadges = htmlDoc.querySelector('#elite-badges')
		var reviewVotes = htmlDoc.querySelector('#review_votes')
		var complements = htmlDoc.querySelector('#userComplimentIcons')
		var userProfile = htmlDoc.querySelector('#profile_questions')

		// COLLECT USER INFO
		userInfo['user_id'] = userId
		userInfo['name'] = parseUserName(title);
		userInfo['elite_year'] = parseEliteBagdes(eliteBadges)
		userInfo['complements'] = parseComplements(complements)
		userInfo['votes'] = parseReviewVotes(reviewVotes)
		// Merge Objects
		jQuery.extend( userInfo, parseUserProfile(userProfile) )
		jQuery.extend( userInfo, parseUserStat(userStats) )

		var QUERY = ""
		if (firstSeed == true) {
			Query = makeInsertQuery("User", userInfo)
			firstSeed = false;
		}
		else {
			QUERY = makeUpdateQuery(userInfo)
		}
		console.log(QUERY)
		doQuery(db, QUERY)
		callbackNum -= 1
	})

	var parseUserName = function(title) {
		var name = title.innerText.split('\'s')[0]
		return name
	}
	var parseUserStat = function(userStats) {
		var result = new Object()
		var anchors = userStats.getElementsByTagName("a")

		for (var i = 0; i < anchors.length; i++) {
			var each = anchors[i];
			// 96 friends
			// 74 reviews
			// etc . . .

			var stat = removeWhiteSpace(each.innerText).split(' ')

			if (stat[1] == 'Friends' || stat[1] == 'Friend') {
				result['friends_num'] = stat[0];
				continue;
			}
			if (stat[1] == 'Reviews' || stat[1] == 'Review') {
				result['reviews_num'] = stat[0]
				continue
			}
			if (stat[1] == 'Firsts' || stat[1] == 'First') {
				result['firsts_num'] = stat[0]
				continue
			}
		}
		return result
	}

	var parseEliteBagdes = function(eliteBadges) {

		if (eliteBadges == null)
			return null

		var eliteYears = []
		var anchors = eliteBadges.getElementsByTagName('a')
		for (var i = 0; i < anchors.length; i++) {
			var badge = anchors[i];
			// elite 2013
			var title = badge.getAttribute("title")
			var year = title.split(' ')[1]
			eliteYears.push(year.substring(2,4))
		}
		eliteYears = eliteYears.join('-')
		return eliteYears
	}
	var parseReviewVotes = function(reviewVotes) {

		if (reviewVotes == null)
			return "0-0-0"

		var votes = reviewVotes.innerText.split('\n')[1]
		votes = removeWhiteSpace(votes).split(' ')
		// votes : 	[0]64 [1]Useful, [2]13 [3]Funny, [4]and [5]20 [6]Cool
		var result = votes[0] + "-" + votes[2] + "-" + votes[5];

		return result
	}
	var parseComplements = function(complements) {

		if (complements == null)
			return 0

		var compTotal = 0
		var compList = removeWhiteSpace(complements.innerText).split(' ')

		for (var i = 0; i < compList.length; i++) {
			
			var compNum = parseInt(compList[i]);
			// if this data is Intager
			// if 2 == '2'
			if (compNum == compList[i])
				compTotal += compNum
		}
		return compTotal
	}
	var parseUserProfile = function(userProfile) {
		var profile = userProfile.innerText.split('\n')
		profile = clearList(profile)
		var result = new Object()
		result['location'] = profile[1]
		result['since'] = profile[3]

		return result
	}

	return userInfo
}


/*
	returns a List of Objects
*/
function parseAndInsertFriendPage(db, userId, start) {
	start = typeof start !== 'undefined' ? start : 0;
	
	var PRE_URL = "http://www.yelp.com/user_details_friends?sort=first_name&userid="
	var POST_URL = "&start="
	var url = PRE_URL + userId + POST_URL + start

	var friendList = []

	getHtmlDoc(url, function(htmlDoc) {
		
		// case of closed user
		if (htmlDoc.querySelector("#inactive_user") != null) {
			callbackNum -= 1
			return
		}

		// GET FRIENDS NUMBER
		var pageInfo = htmlDoc.querySelector("td.range-of-total")
		if (pageInfo == null) { // means 0 friend
			callbackNum -= 1
			return
		}

		var friendsNum = removeWhiteSpace(pageInfo.innerText).split(' ')[4]
		friendsNum = parseInt(friendsNum)

		// PARSE FRIENDS
		var friendBoxes = htmlDoc.querySelectorAll("div.friend_box")
		for (var i = 0; i < friendBoxes.length; i++) {
			var friendBox = friendBoxes[i]
			var friendInfo = parseFriend(friendBox)
			// RESTRICT CONDITION
			// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			if (friendInfo['location'].indexOf('Philadelphia, PA') == -1)
				continue
			// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			friendList.push(friendInfo)
		}
		
		if (friendsNum > (start + 100)) {
			var moreFriends = parseAndInsertFriendPage(db, userId, start + 100)
			friendList = friendList.concat(moreFriends)
		}

		if (start > 0) {
			callbackNum -= 1
			return;
		}

		// INSERT TO DATABASE
		for (var i = 0; i < friendList.length; i++) {

			var friendData = friendList[i]
			if (friendData == undefined) {
				console.log("user: "+ userId + " i: "+ i + "/" + friendList.length)
				callbackNum -= 1
				return
			}
			var friendId = friendData['user_id']

			// insert friend
			QUERY = makeInsertQuery("User", friendData)
			doQuery(db, QUERY)
			
			// insert relation
			var relationData = {'user_id':userId, 'friend_id':friendId}
			QUERY = makeInsertQuery("Friend", relationData)
			doQuery(db, QUERY)
		}
		QUERY = "UPDATE User SET PA_friends_num='" + friendList.length +
				"' WHERE user_id='" + userId + "';"
		doQuery(db, QUERY)

		callbackNum -= 1
	})

	var parseFriend = function(friend) {
		var result = new Object()

		var userName = friend.querySelector("li.user-name")
		var anchor = userName.getElementsByTagName("a")[0]
		var userId = anchor.getAttribute('href').split("=")[1];
		var userLocation = friend.querySelector("li.user-location")

		userName = removeWhiteSpace(userName.innerText)
		if (userName.indexOf('…') != -1) {
			userName = userName.replace('…', '..')
		}

		fnum = removeWhiteSpace(friend.querySelector("li.friend-count").innerText).split(' ')[0];
		rnum = removeWhiteSpace(friend.querySelector("li.review-count").innerText).split(' ')[0];

		result['user_id'] = userId
		result['name'] = userName
		result['location'] = userLocation.innerText
		result['friends_num'] = fnum
		result['reviews_num'] = rnum

		return result
	}

	return friendList
}


/*
	returns an Object about a Business
*/
function parseAndInsertBizPage(db, bizId) {
	var PRE_URL = "http://www.yelp.com/biz/"
	var url = PRE_URL + bizId
	var bizInfo = new Object()

	getHtmlDoc(url, function(htmlDoc) {
		
		var bizTitle = htmlDoc.querySelector("title")
		var bizHeader = htmlDoc.querySelector("#bizInfoHeader")
		var bizCategory = htmlDoc.querySelector("#bizCategories")
		var bizAddress = htmlDoc.querySelector("address")
		var priceTip = htmlDoc.querySelector("#price_tip")

		// COLLECT BIZ INFO
		bizInfo['biz_id'] = bizId
		bizInfo['name'] = parseTitle(bizTitle)
		bizInfo['category'] = parseCategory(bizCategory)
		bizInfo['address'] = parseAddress(bizAddress)
		if (priceTip != null) {
			var price = priceTip.innerText
			bizInfo['price'] = price
		}
		// Merge Objects
		jQuery.extend( bizInfo, parseHeader(bizHeader) )

		/*
			bizInfo['category'] 	(list of list)
			need's to be handled
		*/

		// INSERT INTO DATABASE
		var categories = bizInfo['category']
		delete bizInfo['category']

		var QUERY = makeInsertQuery("Biz", bizInfo)
		doQuery(db, QUERY)

		for (var j = 0; j < categories.length; j++) {
			var conditions = []
			var category = categories[j]
			for (var k = 0; k < category.length; k++) {
				category[k] = category[k].replace("'", "''")
				var condition = "level" + k + "='" + category[k] + "'"
				conditions.push(condition)
			}
			conditions = conditions.join(' AND ')
			var QUERY = "SELECT cat_id FROM Category WHERE " + conditions + ";"
			doQuery(db, QUERY, callbackC.bind(this, bizId));

			function callbackC(bizId, tx, queryResult) {
				if (queryResult.rows.length == 0)
					console.log("CAT ERROR: " + bizId)
				var categoryId = queryResult.rows.item(0)['cat_id']
				var bizcatData = new Object()
				bizcatData['biz_id'] = bizId
				bizcatData['cat_id'] = categoryId
				
				var QUERY = makeInsertQuery("BizCat", bizcatData)
				doQuery(db, QUERY)
			}
		}

		callbackNum -= 1
	})

	

	var parseTitle = function(bizTitle) {
		var name = bizTitle.innerText.split(' - ')[0]
		return name
	}

	var parseHeader = function(bizHeader) {
		var result = new Object()

		var reviewCounter = bizHeader.querySelector("span.review-count")
		if (reviewCounter == null) {
			result['total_rating'] = 0
			result['review_count'] = 0
			return result
		}
		var reviewCount = reviewCounter.innerText.split(' ')[0]

		var bizMetaInfo = bizHeader.querySelector("meta")
		var rating = bizMetaInfo.getAttribute("content")

		result['total_rating'] = rating
		result['review_count'] = reviewCount

		return result
	}

	var parseCategory = function(bizCategory) {
		var result = []

		var categories = bizCategory.querySelectorAll("span.hidden")
		
		// one biz multiple categories
		for (var i = 0; i < categories.length; i++) {
			var category = categories[i]
			var spans = category.querySelectorAll("span")
			var categoryLevel = []
			for (var j = 0; j < spans.length; j++) {
				if (spans[j].getAttribute("itemprop") == "title")
					categoryLevel.push(spans[j].innerText)
			}
			result.push(categoryLevel)
		}
		return result
	}
	var parseAddress = function(bizAddress) {
		var spans = bizAddress.querySelectorAll("span")
		var address = []
		for (var i = 0; i < spans.length; i++) {
			var span = spans[i]
			address.push(span.innerText)
		}
		address = address.join().replace('\n', ',')

		return address
	}
	return bizInfo
}

function parseAndInsertReviewPage(db, userId, start) {
	start = typeof start !== 'undefined' ? start : 0;

	var PRE_URL = "http://www.yelp.com/user_details_reviews_self?userid="
	var POST_URL = "&rec_pagestart="
	// RESTRICT CONDITION
	// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	var RESTRICT = "&review_filter=location&location_filter_city=Philadelphia&location_filter_state=PA&review_sort=time"
	// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	var url = PRE_URL + userId + RESTRICT + POST_URL + start

	var reviewList = []
	getHtmlDoc(url, function(htmlDoc) {
		//  GET REVIEW NUMBER
		var pageInfo = htmlDoc.querySelector("td.range-of-total")
		if (pageInfo == null) {
			// means 0 review
			callbackNum -= 1
			return reviewList
		}
		var reviewsNum = removeWhiteSpace(pageInfo.innerText).split(' ')[4]
		reviewsNum = parseInt(reviewsNum)
		
		//  PARSE REVIEW
		var reviews = htmlDoc.querySelectorAll("div.review")
		for (var i = 0; i < reviews.length; i++) {
			var review = reviews[i]
			var reviewInfo = parseReview(review)
			reviewInfo['writer_id'] = userId

			var previous = reviewInfo['old']
			if (previous != null) {
				for (var j = 0; j < previous.length; j++) {
					previous[j]['writer_id'] = userId;
					reviewList.push(previous[j])
				}
				delete reviewInfo['old']
			}
			reviewList.push(reviewInfo)
		}

		if (reviewsNum > (start + 10)) {
			var moreReviews = parseAndInsertReviewPage(db, userId, start + 10)
			reviewList = reviewList.concat(moreReviews)
		}

		if (start > 0) {
			callbackNum -= 1
			return
		}
		// INSERT INTO DATABASE
		for (var i = 0; i < reviewList.length; i++) {
			var reviewData = reviewList[i]
			var bizId = reviewData['biz_id']

			// insert review
			var QUERY = makeInsertQuery("Review", reviewData)
			doQuery(db, QUERY)
			
			// insert biz
			parseAndInsertBizPage(db, bizId)
		}

		QUERY = "UPDATE User SET PA_reviews_num='" + reviewList.length +
				"' WHERE user_id='" + userId + "';"
		doQuery(db, QUERY)

		callbackNum -= 1
	})
	

	var parseReview = function(review) {
		var result = new Object()

		var bizInfo = review.querySelector("div.biz_info")
		var reviewMeta = review.querySelector("div.review-meta")
		var reviewText = review.querySelector("div.review_comment")

		// REVIEW ABOUT
		var bizLink = bizInfo.querySelector("h4 a")["href"]
		var start = bizLink.indexOf('/biz/') + 5
		var end = bizLink.indexOf('#')
		var bizId = bizLink.substring(start, end)

		// META DATA
		var ratingStar = reviewMeta.querySelector("i")
		var rating = ratingStar.getAttribute("title").split(' ')[0]
		
		var dateSpan = reviewMeta.querySelector("span.date")
		var postDate = dateSpan.innerText.replace(/\s/g, '');
		// case of "Update-11/13/2013"
		if (postDate.indexOf('-') != -1)
			postDate = postDate.split('-')[1]
		
		// REVIEW TEXT
		var reviewText = removeWhiteSpace(reviewText.innerText)

		result['biz_id'] = bizId
		result['review_rating'] = rating
		result['post_date'] = postDate
		result['review_text'] = reviewText


		// Previous Review
		var oldReviews = review.querySelectorAll("li.old-review")
		if (oldReviews != null) {
			result['old'] = []
			var oldResult = new Object()
			for (var i = 0; i < oldReviews.length; i++) {
				var oldReview = oldReviews[i]
				var ratingStar = oldReview.querySelector("i")
				var rating = ratingStar.getAttribute("title").split(' ')[0]
				var dateEm = oldReview.querySelector("em")
				var postDate = dateEm.innerText.replace(/\s/g, '');
				var reviewText = oldReview.querySelector("p.review_comment")
				var review = removeWhiteSpace(reviewText.innerText)

				oldResult['biz_id'] = bizId
				oldResult['review_rating'] = rating
				oldResult['post_date'] = postDate
				oldResult['review_text'] = review
				result['old'].push(oldResult)
			}
		}


		return result
	}

	return reviewList
}

