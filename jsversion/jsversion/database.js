/*
	Written by FourwingsY
	Written at 2013. 12. 14.
	version 0.3
*/

function startDB() {
	var db = openDatabase('mydb', '1.0', 'Test DB', 10 * 1024 * 1024);
	return db
}

function insertQuery(db, QUERY) {
	db.transaction(function (tx) {
		// console.log(QUERY)
		tx.executeSql(QUERY);
	});
}

function createUserTable(db) {

	var QUERY = "CREATE TABLE User (" +
		"	userid CHAR(22) PRIMARY KEY NOT NULL," +
		"	name VARCHAR(30) NOT NULL," +
		"	location VARCHAR(30) NOT NULL," +
		"	since VARCHAR(15)," +
		"	friends_num INT NOT NULL DEFAULT -1," +
		"	reviews_num INT NOT NULL DEFAULT -1," +
		"	firsts_num INT," +
		"	elite VARCHAR(30)," +
		"	votes VARCHAR(20)," +
		"	complements INT," +
		"	updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"

	insertQuery(db, QUERY);
}

function createFriendTable(db) {

	var QUERY = "CREATE TABLE Friend (" +
		"	userid CHAR(22) NOT NULL," +
		"	friendid CHAR(22) NOT NULL," +
		"	FOREIGN KEY (userid)" +
		"		REFERENCES User(userid)" +
		"		ON UPDATE CASCADE ON DELETE RESTRICT," +
		"	FOREIGN KEY (friendid)" +
		"		REFERENCES User(userid)" +
		"		ON UPDATE CASCADE ON DELETE RESTRICT)"
	
	insertQuery(db, QUERY);
}

function makeInsertQuery(table_name, data) {
	
	// ORDERING DATA
	var query_column = []
	var query_value = []

	for (key in data) {
		var value = data[key]
		value = handleApostrophe(value)
		query_column.push(key)
		query_value.push(value)
	}
		
	column_count = query_column.length;

	// MAKE QUERY
	var QUERY = "INSERT OR REPLACE INTO " + table_name + " ("
	for (var i = 0; i < column_count; i++) {
		QUERY += query_column[i] + ', '
	}
	QUERY = QUERY.substr(0, QUERY.length-2) + ") "
		
	QUERY += "VALUES ("
	for (var i = 0; i < column_count; i++) {
		QUERY += "'" + query_value[i] + "', "
	}
	QUERY = QUERY.substr(0, QUERY.length-2) + ");"

	// " ON DUPLICATE KEY UPDATE "
	
	// for (var i = 0; i < column_count; i++) {
	// 	QUERY += query_column[i] + "='" + query_value[i] + "', "
	// }

	return QUERY
}

function handleApostrophe(string) {

	splited = string.split("'")
	edited = splited.join("\\'")
	return edited
}

function getPrimaryKeys(table_name) {

	if (table_name == "User")
		return ["userid"]
	else if (table_name == "Biz")
		return ["biz_url"]
	else if (table_name == "Review")
		return ["writerid", "biz_url"]
	else if (table_name == "Friend")
		return ["userid", "friendid"]
}

function selectQuery(db, QUERY, callback) {
	db.transaction(function (tx) {
		tx.executeSql(QUERY, [], callback, null);
	});
}

function insertUserData(db, user) {

	// MAKE MULTI-DATA TO SINGLE-STRING

	var votes = user['votes']
	var elite = user['elite']
	
	if (votes != undefined)
		user['votes'] = handleVoteInfo(votes)
	if (elite != undefined)
		user['elite'] = handleEliteInfo(elite)

	// MAKE QUERY
	var QUERY = makeInsertQuery("User", user)
	if (QUERY != null) 
		insertQuery(db, QUERY)
}

function insertFriendData(db, userid, friendid) {

	var friend = {'userid':userid, 'friendid':friendid}
	var QUERY = makeInsertQuery("Friend", friend)

	if (QUERY != null)
		insertQuery(db, QUERY)

}

function handleVoteInfo(votes) {
	// {'votes':{'funny':'123', 'useful':'52', 'cool':'156'} }
	// -> '123-52-156'
	vote_info = [votes['funny'], votes['useful'], votes['cool']]

	return vote_info.join('-')
}

function handleEliteInfo(elite) {
	// ['2013', '2012', '2011', '2010']
	// -> '13-12-11-10'
	years = []
	for (var i = 0; i < elite.length; i++){
		year = elite[i].substr(2,2)
		years.push(year)
	}
	return years.join('-')
}