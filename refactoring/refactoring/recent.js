function parseRecent() {
	IS_CODE_RUNNING = true

	var QUERY = "select post_date from (select post_date from review) order by post_date desc limit 1"
	doQuery(db, QUERY, function(tx, queryResult) {
		console.log("oh my...")
		lastDateInDB = queryResult.rows.item(0)["post_date"]
		parseRecentActivity(db, lastDateInDB)
	})

	function parseRecentActivity(db, lastDateInDB) {
		var URL = "http://www.yelp.com/philadelphia"
		var iframe = document.querySelector("#viewer")
		iframe.setAttribute("src", URL);

		// GET MORE REVIEWS		
		$('iframe').load(function() {
			var htmlDoc = iframe.contentDocument;
			var activityFeed = htmlDoc.querySelector("#activity-feed")

			// FOR EVERY 20 ACTIVITY LOADED
			var load = setInterval(function() {

				// SEE MORE
				var activities = activityFeed.querySelector("ul.ylist")
				var seeMore = activityFeed.querySelector("a.link-bar")
				seeMore.click()

				// check if activity showing now have to be parsed or nat
				var lastActivity = activities.lastElementChild
				var lastActivityDate = parseActivity(lastActivity)['post_date']
				console.log("last: " + lastActivityDate)
				console.log("from DB: " + lastDateInDB)

				if (lastActivityDate < lastDateInDB) {
					clearInterval(load)
					// STOP!!
				}

				var len = activities.childElementCount
				console.log(len)

				for (var i = 0; i < len; i++) {
					var activity = activities.children[i]
					if (activity.className.indexOf("review-block") == -1) {
						// NOT REVIEW BLOCK. IGNORE THIS
						continue;
					}

					// PARSE AND SAVE!
					activity_info = parseActivity(activity)
					
					parseAndInsertUserPage(db, activity_info['writer_id'])
					parseAndInsertBizPage(db, activity_info['biz_id'])
					
					var query = makeInsertQuery("Review", activity_info)
					doQuery(db, query)
				}

				// DELETE FROM viewer AFTER PARSE
				for (var i = 0; i < len; i++) {
					activities.removeChild(activities.children[0])
				}


			}, 10000)
		})


	}

	function parseActivity(activity) {
		var userAnchor = activity.querySelector("a.user-name")
		var userId = userAnchor.getAttribute("href").split("userid=")[1]
		var bizAnchor = activity.querySelector("a.biz-name")
		var bizId = bizAnchor.getAttribute("href").split("biz/")[1].split("#")[0]

		var contentElement = activity.querySelector("p.js-content-expandable")
		if (contentElement.childElementCount == 1) {
			// FOR SHORT TEXT
			var content = contentElement.firstElementChild.innerText
		}
		else {
			// FOR LONG TEXT
			var content = contentElement.lastElementChild.innerText
		}

		var rating = activity.querySelector("i").getAttribute("title").split(' ')[0]

		var dateSpan = activity.querySelector("span.rating-qualifier")
		if (dateSpan == null) {
			// IF this activity is not review
			// return NOW : continue parsing
			var postDate = getDateOfNow()
		}
		else {
			var postDate = yelpDateToCommonDate(dateSpan.innerText)
		} 

		return {"writer_id":userId, "biz_id":bizId, "review_text":content, "review_rating":rating, "post_date":postDate}
	}
}