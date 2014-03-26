/*
	Written by FourwingsY
	Written at 2014. 03. 22.
	version 0.6
*/


function getHtmlDoc(_url, callback, nojs, noimg) {
	var htmlString = null;

	if (nojs == undefined || nojs == null)
		nojs = true;
	if (noimg == undefined || noimg == null)
		noimg = true;

	callbackNum += 1;

	$.ajax({
		url: _url,
		type: 'GET',
		success: function(result) {
			htmlString = result;

			// remove script or img tag
			if (nojs) {
				htmlString = htmlString.replace(/<script/g, "<sccc ")
				htmlString = htmlString.replace(/script>/g, "sccc>")
			}
			if (noimg)
				htmlString = htmlString.replace(/<img/g, "<immmmm ")

			var htmlDoc = document.createElement('html');
			htmlDoc.innerHTML = htmlString;

			callback(htmlDoc);
		}
	})
}


function parseAndInsertUserPage(db, userId) {
	var PRE_URL = "http://www.yelp.com/user_details?userid="
	var URL = PRE_URL + userId
	var userInfo = new Object()

	getHtmlDoc(URL, function(htmlDoc) {
		console.log(callbackNum);
		
		// case of closed user
		if (htmlDoc.querySelector('#inactive_user') != null) {
			userInfo['user_id'] = userId
			// userInfo['name'] = "closed"
			userInfo['since'] = "closed"

			QUERY = makeInsertQuery("User", userInfo)
			doQuery(db, QUERY)

			callbackNum -= 1
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

		var QUERY = makeInsertQuery("User", userInfo)
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

			if (stat[1].indexOf('Friend') != -1) {
				result['friends_num'] = stat[0];
				continue;
			}
			if (stat[1].indexOf('Review') != -1) {
				result['reviews_num'] = stat[0]
				continue
			}
			if (stat[1].indexOf('First') != -1) {
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
			var year = title.split(' ')
			year = year[year.length-1]
			eliteYears.push(year.substring(2,4))
		}
		eliteYears = eliteYears.join('m')
		return eliteYears
	}
	var parseReviewVotes = function(reviewVotes) {

		if (reviewVotes == null)
			return "0m0m0"

		var votes = reviewVotes.innerText.split('\n')[1]
		votes = removeWhiteSpace(votes).split(' ')
		// votes : 	[0]64 [1]Useful, [2]13 [3]Funny, [4]and [5]20 [6]Cool
		var result = votes[0] + "m" + votes[2] + "m" + votes[5];

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
}


function parseAndInsertFriendPage(db, userId, start) {
	start = (typeof start !== 'undefined' ? start : 0);
	
	var PRE_URL = "http://www.yelp.com/user_details_friends?sort=first_name&userid="
	var POST_URL = "&start="
	var URL = PRE_URL + userId + POST_URL + start

	var friendList = []

	getHtmlDoc(URL, function(htmlDoc) {
		
		// case of closed user
		if (htmlDoc.querySelector("#inactive_user") != null) {
			var QUERY = "UPDATE User SET PA_friends_num = 0 WHERE user_id='" + userId + "';"
			doQuery(db, QUERY)
			callbackNum -= 1
			return
		}

		// GET FRIENDS NUMBER
		var pageInfo = htmlDoc.querySelector("td.range-of-total")
		if (pageInfo == null) {
			// means 0 friend
			var QUERY = "UPDATE User SET PA_friends_num = 0 WHERE user_id='" + userId + "';"
			doQuery(db, QUERY)
			QUERY = "UPDATE User SET friends_num = 0 WHERE user_id='" + userId + "';"
			doQuery(db, QUERY)
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
		
		if (friendsNum >= (start + 100))
			parseAndInsertFriendPage(db, userId, start + 100)

		var PA_FRIEND = friendList.length
		// INSERT TO DATABASE
		for (var i = 0; i < PA_FRIEND; i++) {

			var friendData = friendList[i]
			if (friendData == undefined) {
				console.error("user: "+ userId + " i: "+ (start+i) + "/" + (start+PA_FRIEND))
				continue
			}

			var friendId = friendData['user_id']

			// insert friend only if friend is not in db
			var QUERY = "SELECT user_id from User where user_id='" + friendId + "';"
			doQuery(db, QUERY, callbackF.bind(this, friendData))
			function callbackF (friendData, tx, result) {
				if (result.rows.length == 0) {
					var QUERY = makeInsertQuery("User", friendData)
					doQuery(db, QUERY)
				}
			}
			
			// insert relation
			var relationData = {'user_id':userId, 'friend_id':friendId}
			QUERY = makeInsertQuery("Friend", relationData)
			doQuery(db, QUERY)
		}
		QUERY = "SELECT PA_friends_num from User where user_id='" + userId + "';"
		doQuery(db, QUERY, function(tx, result) {
			if (result.rows.item(0)['PA_friends_num'] == -1) {
				QUERY = "UPDATE User SET PA_friends_num=" + PA_FRIEND +
					" WHERE user_id='" + userId + "';"
			}
			else {
				QUERY = "UPDATE User SET PA_friends_num=PA_friends_num+" + PA_FRIEND +
					" WHERE user_id='" + userId + "';"
			}
			doQuery(db, QUERY)
		})
		
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


function parseAndInsertBizPage(db, bizId) {
	var PRE_URL = "http://www.yelp.com/biz/"
	var URL = PRE_URL + bizId
	
	var bizInfo = new Object()

	getHtmlDoc(URL, function(htmlDoc) {
		
		var bizTitle = htmlDoc.querySelector("title")
		var bizRating = htmlDoc.querySelector("div.rating-info")
		var bizCategory = htmlDoc.querySelector("span.category-str-list")
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
		jQuery.extend( bizInfo, parseHeader(bizRating) )

		/*
			bizInfo['category'] 	(String list)
			need's to be handled
		*/

		// INSERT INTO DATABASE
		var categories = bizInfo['category']
		delete bizInfo['category']

		var QUERY = makeInsertQuery("Biz", bizInfo)
		doQuery(db, QUERY)

		for (var j = 0; j < categories.length; j++) {
			var category = categories[j]

			var QUERY = "SELECT cat_id FROM Category WHERE level1 = '" + category +
						"' or level2 = '" + category + "';"
			doQuery(db, QUERY, callbackC.bind(this, bizId));

			function callbackC(bizId, tx, queryResult) {
				if (queryResult.rows.length == 0) {
					console.error("CAT ERROR: " + bizId)
					return
				}
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

	var parseHeader = function(bizRating) {
		var result = new Object()

		var reviewCounter = bizRating.querySelector("span.review-count")
		if (reviewCounter == null) {
			result['total_rating'] = 0
			result['review_count'] = 0
			return result
		}
		var reviewCount = reviewCounter.innerText.split(' ')[0]

		var bizMetaInfo = bizRating.querySelector("meta")
		var rating = bizMetaInfo.getAttribute("content")

		result['total_rating'] = rating
		result['review_count'] = reviewCount

		return result
	}

	var parseCategory = function(bizCategory) {
		var result = []

		var categories = bizCategory.querySelectorAll("a")
		
		// one biz multiple categories
		for (var i = 0; i < categories.length; i++) {
			var category = categories[i]
			result.push(category.innerText)
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
}

function parseAndInsertReviewPage(db, userId, start) {
	start = (typeof start !== 'undefined' ? start : 0)

	var PRE_URL = "http://www.yelp.com/user_details_reviews_self?userid="
	var POST_URL = "&rec_pagestart="
	// RESTRICT CONDITION
	// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	var RESTRICT = "&review_filter=location&location_filter_city=Philadelphia&location_filter_state=PA&review_sort=time"
	// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	var URL = PRE_URL + userId + RESTRICT + POST_URL + start

	var reviewList = []

	getHtmlDoc(URL, function(htmlDoc) {
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
			if (reviewInfo["review_text"] == null) {
				console.error("deleted review: " + userId);
			}
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

		if (reviewsNum > (start + 10))
			parseAndInsertReviewPage(db, userId, start + 10)

		// INSERT INTO DATABASE
		for (var i = 0; i < reviewList.length; i++) {
			var reviewData = reviewList[i]
			var bizId = reviewData['biz_id']

			// insert biz only if biz is not in db
			QUERY = "SELECT biz_id from Biz where biz_id='" + bizId + "';"
			doQuery(db, QUERY, callbackB.bind(this, bizId))
			function callbackB (bizId, tx, result) {
				if (result.rows.length == 0)
					parseAndInsertBizPage(db, bizId)
			}

			// insert review
			var QUERY = makeInsertQuery("Review", reviewData)
			doQuery(db, QUERY)
		}

		if (reviewList == null || reviewList.length == 0) {
			console.log("PA_reviews_num = 0")
			QUERY = "UPDATE User SET PA_reviews_num = 0" +
				" WHERE user_id='" + userId + "';"
			doQuery(db, QUERY)
			callbackNum -= 1
			return
		}

		QUERY = "SELECT PA_reviews_num from User where user_id = '" + userId + "';"
		doQuery(db, QUERY, function(tx, result) {
			if (result.rows.item(0)['PA_reviews_num'] == -1)
				QUERY = "UPDATE User SET PA_reviews_num = " + reviewList.length +
				" WHERE user_id='" + userId + "';"
			else 
				QUERY = "UPDATE User SET PA_reviews_num = PA_reviews_num + " + reviewList.length +
				" WHERE user_id='" + userId + "';"
			doQuery(db, QUERY)
		})
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
		
		result['biz_id'] = bizId
		result['review_rating'] = rating
		result['post_date'] = yelpDateToCommonDate(postDate)

		// REVIEW TEXT
		if (reviewText == null) {
			console.error(bizId + " / " + postDate);
		}
		else {
			reviewText = removeWhiteSpace(reviewText.innerText)
			result['review_text'] = reviewText
		}
		

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
}

