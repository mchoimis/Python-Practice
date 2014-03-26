/*
	Written by FourwingsY
	Written at 2014. 03. 22.
	version 0.6
*/

function startDB() {
	// DB name: yelp, size: 10MB
	var db = openDatabase('yelp', '1.0', 'Parsed Data from Yelp.com', 100 * 1024 * 1024);
	return db
}

function doQuery(db, QUERY, callback) {
	db.transaction(function (tx) {
		if (callback == null)
			tx.executeSql(QUERY, [], null, errorCallback);
		else
			tx.executeSql(QUERY, [], callback, errorCallback);
		
		/********** DEBUGGING ************/
		// console.log(QUERY)

		function errorCallback(tx, error) {
			console.error("ERROR: " + error.message + " at QUERY: " + QUERY);
		}
	});
}

function makeInsertQuery(tableName, data) {
	
	// data: JS Object
	// ORDERING DATA
	var queryKey = []
	var queryValue = []

	for (key in data) {
		var value = data[key]
		if (value == null)
			continue
		value = handleApostrophe(value)
		queryKey.push(key)
		queryValue.push(value)
	}
	columnCount = queryKey.length;

	// MAKE QUERY
	// INSERT OR REPLACE INTO USER (user_id, name, ....)
	// VALUES ('qwe123ASDzxc', 'John C.', ...);

	var QUERY = "INSERT OR REPLACE INTO " + tableName + " ("
	for (var i = 0; i < columnCount; i++) {
		QUERY += queryKey[i] + ', '
	}
	QUERY = QUERY.substr(0, QUERY.length-2) + ") "
	
	QUERY += "VALUES ("
	for (var i = 0; i < columnCount; i++) {
		QUERY += "'" + queryValue[i] + "', "
	}
	QUERY = QUERY.substr(0, QUERY.length-2) + ");"
	return QUERY
}

function makeUpdateQuery(tableName, data) {
	var queryKey = []
	var queryValue = []

	for (key in data) {
		var value = data[key]
		if (value == null)
			continue
		value = handleApostrophe(value)
		queryKey.push(key)
		queryValue.push(value)
	}
	columnCount = queryKey.length;

	var getPrimaryKey = function(tableName) {
		var tableKeyDict = {
			"User":"user_id",
			"Biz":"biz_id"
		}
		return tableKeyDict["tableName"]
	}

	var QUERY = "UPDATE User SET "
	for (var i = 0; i < columnCount; i++) {
		QUERY += queryKey[i] + "='" + queryValue[i] + "', "
	}
	QUERY = QUERY.substr(0, QUERY.length-2) +
			" WHERE " + getPrimaryKey(tableName) + "='" +
			data[getPrimaryKey(tableName)] + "';"

	return QUERY
}

function handleApostrophe(string) {
	if (typeof string != "string") return string;
	splited = string.split("'")
	edited = splited.join("''")
	return edited
}

function createUserTable(db) {

	var QUERY = "CREATE TABLE User (" +
		"	user_id CHAR(22) NOT NULL," +
		"	u_index INT AUTOINCREMENT," +
		"	name VARCHAR(30)," +
		"	location VARCHAR(30)," +
		"	since VARCHAR(15)," +
		"	friends_num INT," +
		"	reviews_num INT," +
		"	PA_friends_num INT DEFAULT -1," +
		"	PA_reviews_num INT DEFAULT -1," +
		"	firsts_num INT," +
		"	elite_year VARCHAR(30)," +
		"	votes VARCHAR(20)," +
		"	complements INT," +
		"	updated VARCHAR(50) );"

	doQuery(db, QUERY, null);
}

function createFriendTable(db) {

	var QUERY = "CREATE TABLE Friend (" +
		"	user_id CHAR(22) NOT NULL," +
		"	u_index INT," +
		"	friend_id CHAR(22) NOT NULL," +
		"	f_index INT);"
	
	doQuery(db, QUERY, null);
}

function createBizTable(db) {
	var QUERY = "CREATE TABLE Biz (" +
		"	biz_id CHAR(50) PRIMARY KEY NOT NULL," +
		"	b_index INT," + 
		"	name VARCHAR(50) NOT NULL," +
		"	total_rating FLOAT NOT NULL," +
		"	review_count INT NOT NULL," +
		"	address VARCHAR(100)," +
		"	price VARCHAR(5)," +
		"	updated VARCHAR(50) );"
	
	doQuery(db, QUERY, null);
}

function createReviewTable(db) {
	var QUERY = "CREATE TABLE Review (" +
		"	writer_id CHAR(22) NOT NULL," +
		"	u_index INT," + 
		"	biz_id CHAR(50) NOT NULL," +
		"	b_index INT," +
		"	post_date DATE NOT NULL," +
		"	review_rating FLOAT NOT NULL," +
		"	review_text LONGTEXT);"
	
	doQuery(db, QUERY, null);
}

function createBizCatTable(db) {
	var QUERY = "CREATE TABLE BizCat (" +
		"	biz_id CHAR(50) NOT NULL," +
		"	cat_id INT NOT NULL);"

	doQuery(db, QUERY, null);
}
