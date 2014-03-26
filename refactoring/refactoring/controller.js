// EVERYDAY RUNNING
function startIntervalFunction() {
	lastCBNum = 0
	
	var isDayToReParse = function() {
		var PARSING_DAY = 0 // MEANS SUNDAY
		var now = new Date()
		if (now.getDay() == PARSING_DAY && now.getHours() < 5) {
			return true
		}
		return false
	}

	var startParser = setInterval(function() {
		if (IS_CODE_RUNNING == true)
			return

		if (isDayToReParse()) {
			setTaskText("Check User Changed")
			reParse()
		} else {
			setTaskText("Parse Recent Activity")
			parseRecent()
		}
	}, PARSER_INTERVAL)

	var showStatus = setInterval(function() {
		if (IS_CODE_RUNNING) {
			setStatusText("Running now... " + callbackNum)
		} else {
			setStatusText("waiting... ")
		}
	}, STATUS_SHOWING_INTERVAL)

	var checkActualRunning = setInterval(function() {
		if (lastCBNum == callbackNum) {
			// CODE FREEZED!!
			callbackNum = 0
			lastCBNum = 0
			IS_CODE_RUNNING = false
			return
		} else {
			lastCBNum = callbackNum
			setStatusText("parsing " + callbackNum + "pages...")
		}
	}, CHECK_RUNNING_INTERVAL)
}

// FIRST TIME DATA CRAWLING
function crawlData() {

}

function goOrStop(intervalId) {
	if (STOP_SIGN == true) {
		clearInterval(intervalId)
	}
}