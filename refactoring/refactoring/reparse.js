function reParse() {
	IS_CODE_RUNNING = true

	var QUERY = "select user_id, friends_num, reviews_num from User";
	doQuery(db, QUERY, function(tx, result) {
		var userNum = result.rows.length;
		console.log(userNum)
		var i = 0
		var pu = setInterval( function() {
			if (i >= userNum) {
				clearInterval(pu)
			}
			// make random interval : 150 + (0 - 200) ms
			var rand = Math.floor((Math.random()*200));
			setTimeout( function() {
				var userId = result.rows.item(i)['user_id']
				ifUserChangedThenDoThis(userId)
				i++
			}, rand)
		}, 150 );
	})
}

function ifUserChangedThenDoThis(userId) {
	var PRE_URL = "http://www.yelp.com/user_details?userid="
	var URL = PRE_URL + userId

	var parseUserName = function(title) {
		var name = title.innerText.split('\'s')[0]
		return name
	}
	var parseUserStat = function(userStats) {
		var result = new Object()
		var anchors = userStats.getElementsByTagName("a")


		result['friends_num'] = 0
		result['reviews_num'] = 0
		result['firsts_num'] = 0

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
	getHtmlDoc(URL, function(htmlDoc) {
		console.log(URL)
		var userInfo = {}

		if (htmlDoc.querySelector('#inactive_user') != null) {
			userInfo['user_id'] = userId
			// userInfo['name'] = "closed"
			userInfo['since'] = "closed"

			// DO SOMETHING FOR CLOSED USER
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


		// CHECK CHANGE
		var QUERY = "select * from User where user_id = '" + userId + "';"
		doQuery(db, QUERY, function(tx, result) {
			var userDB = result.rows.item(0)
			
			if (userDB['friends_num'] != userInfo['friends_num']) {
				console.log(userId + " - friends_num changed")
				// RESET FRIEND INFO
				QUERY = "UPDATE User SET friends_num=" + userInfo['friends_num'] + " where user_id = '" + userId + "';"
				doQuery(db, QUERY)
				QUERY = "UPDATE User SET PA_friends_num=-1 where user_id = '" + userId + "';"
				doQuery(db, QUERY)
				
				// ENTER NEW INFO
				parseAndInsertFriendPage(db, userId)
			}
/*			
			if (userDB['reviews_num'] != userInfo['reviews_num']) {
				console.log(userId + " - reviews_num changed")
				// RESET REVIEW INFO
				QUERY = "UPDATE User SET reviews_num=0, PA_friends_num=-1 where user_id = '" + userId + "';"
				doQuery(db, QUERY)
				
				// ENTER NEW INFO
				parseAndInsertReviewPage(db, userId)
			}
*/			
			// FOR OTHER INFO
			if (userDB['complements'] != userInfo['complements'] ||
				userDB['votes'] != userInfo['votes'] ||
				userDB['firsts_num'] != userInfo['firsts_num'] ||
				userDB['location'] != userInfo['location'] ||
				userDB['elite_year'] != userInfo['elite_year']) {

				console.log(userId + " - user info changed")
				if (userDB['complements'] != userInfo['complements'])
					console.log("complements: " + userDB['complements'] + ' -> ' + userInfo['complements'])
				if (userDB['votes'] != userInfo['votes'])
					console.log("votes: " + userDB['votes'] + ' -> ' + userInfo['votes'])
				if (userDB['firsts_num'] != userInfo['firsts_num'])
					console.log("first_num: " + userDB['firsts_num'] + ' -> ' + userInfo['firsts_num'])
				if (userDB['location'] != userInfo['location'])
					console.log("location: " + userDB['location'] + ' -> ' + userInfo['location'])
				if (userDB['elite_year'] != userInfo['elite_year'])
					console.log("elite_year: " + userDB['elite_year'] + ' -> ' + userInfo['elite_year'])				

				QUERY = "UPDATE User SET " + 
						"complements=" + userInfo['complements'] + ", " +
						"votes='" + userInfo['votes'] + "', " +
						"firsts_num=" + userInfo['firsts_num'] + ", " +
						"location='" + userInfo['location'] + "', " +
						"elite_year='" + userInfo['elite_year'] + "' where " +
						"user_id='" + userId + "';"
				doQuery(db, QUERY);
			}

			QUERY = "UPDATE User SET updated='" + getDateOfNow() + "' where user_id = '" + userId + "';"
			doQuery(db, QUERY)

		})
	})
}