function start() {
	console.log("start")
	setTaskText("START PARSING")
	startIntervalFunction()
}

function stop() {
	STOP_SIGN = true
	setTaskText("PAUSING...")
}

function reset() {
	doQuery(db, "DROP TABLE Review");
	doQuery(db, "DROP TABLE Friend");
	doQuery(db, "DROP TABLE BizCat");
	doQuery(db, "DROP TABLE Biz");
	doQuery(db, "DROP TABLE User");
	doQuery(db, "DROP TABLE Category");
	createUserTable(db)
	createFriendTable(db)
	createCategoryTable(db)
	createBizTable(db)
	createBizCatTable(db)
	createReviewTable(db)
	insertCategoryData(db)
	setStatusText("DATABASE RESET COMPLETE")
}

function setTaskText(text) {
	text = (typeof text == 'undefined' ? TASK_TEXT : text)
	var status = document.getElementById("task");
	status.innerText = text;
}

function setStatusText(text) {
	text = (typeof text == 'undefined' ? STATUS_TEXT : text)
	var status = document.getElementById("status");
	status.innerText = text;
}