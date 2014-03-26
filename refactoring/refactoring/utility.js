function removeWhiteSpace(text) {
	// REPLACE LONG-SPACE to SHORT-SPACE
	var tempText = text.replace(/\s+/g, ' ');
	var length = tempText.length
	
	var startSpace = 0
	var endSpace = 0

	if (tempText[0] == ' ')
		var startSpace = 1
	if (tempText[length-1] == ' ')
		var endSpace = 1

	// REMOVE START & END SHORT-SPACE
	if (startSpace + endSpace > 0)
		tempText = tempText.slice(startSpace, length - endSpace)
	return tempText
}

function clearList(list) {
	// REMOVE WHITE-SPACE to ALL STRING IN THE LIST
	var newList = []
	for (var i = 0; i < list.length; i++) {
		if (list[i] == "") 
			continue
		else newList.push(removeWhiteSpace(list[i]))
	}
	return newList
}

function yelpDateToCommonDate(yelpDate) {
	// m/d/yyyy -> yyyy-mm-dd
	mdy = yelpDate.split('/')
	year = mdy[2]
	month = mdy[0]
	if (month < 10)
		month = '0'+month
	date = mdy[1]
	if (date < 10)
		date = '0'+date
	ymd = [year, month, date]
	return ymd.join('-')
}

function getDateOfNow() {
	var now = new Date()
	var year = now.getFullYear()
	var month = now.getMonth() + 1
	var date = now.getDate()

	return year + '-'  + month + '-' + date
}