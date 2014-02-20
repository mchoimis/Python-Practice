/*
	Written by FourwingsY
	Written at 2013. 12. 3.
	version 0.4
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

		function errorCallback(tx, error) {
			console.log("ERROR: " + error.message + " at QUERY: " + QUERY);
		}
	});
}

function makeInsertQuery(tableName, data) {
	
	// data: JS Object (similar to python dictionary)
	// ORDERING DATA
	var queryKey = []
	var queryValue = []

	var handleApostrophe = function(string) {
		if (typeof string != "string") return string;
		splited = string.split("'")
		edited = splited.join("''")
		return edited
	}

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

function makeUpdateQuery(data) {
	var queryKey = []
	var queryValue = []

	var handleApostrophe = function(string) {
		if (typeof string != "string") return string;
		splited = string.split("'")
		edited = splited.join("''")
		return edited
	}

	for (key in data) {
		var value = data[key]
		if (value == null)
			continue
		value = handleApostrophe(value)
		queryKey.push(key)
		queryValue.push(value)
	}
	columnCount = queryKey.length;

	var QUERY = "UPDATE User SET "
	for (var i = 0; i < columnCount; i++) {
		QUERY += queryKey[i] + "='" + queryValue[i] + "', "
	}
	QUERY = QUERY.substr(0, QUERY.length-2) + " WHERE user_id='" + data['user_id'] + "';"

	return QUERY
}
function createUserTable(db) {

	var QUERY = "CREATE TABLE User (" +
		"	user_id CHAR(22) PRIMARY KEY NOT NULL," +
		"	name VARCHAR(30)," +
		"	location VARCHAR(30)," +
		"	since VARCHAR(15)," +
		"	friends_num INT," +
		"	reviews_num INT," +
		"	PA_friends_num INT," +
		"	PA_reviews_num INT," +
		"	firsts_num INT," +
		"	elite_year VARCHAR(30)," +
		"	votes VARCHAR(20)," +
		"	complements INT," +
		"	updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"

	doQuery(db, QUERY, null);
}

function createFriendTable(db) {

	var QUERY = "CREATE TABLE Friend (" +
		"	user_id CHAR(22) NOT NULL," +
		"	friend_id CHAR(22) NOT NULL);"
	
	doQuery(db, QUERY, null);
}

function createBizTable(db) {
	var QUERY = "CREATE TABLE Biz (" +
		"	biz_id CHAR(50) PRIMARY KEY NOT NULL," +
		"	name VARCHAR(50) NOT NULL," +
		"	total_rating FLOAT NOT NULL," +
		"	review_count INT NOT NULL," +
		"	address VARCHAR(100)," +
		"	price VARCHAR(5)," +
		"	updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
	
	doQuery(db, QUERY, null);
}

function createReviewTable(db) {
	var QUERY = "CREATE TABLE Review (" +
		"	writer_id CHAR(22) NOT NULL," +
		"	biz_id CHAR(50) NOT NULL," +
		"	post_date DATE NOT NULL," +
		"	review_rating FLOAT NOT NULL," +
		"	review_text LONGTEXT);"
	
	doQuery(db, QUERY, null);
}

function createCategoryTable(db) {
	var QUERY = "CREATE TABLE Category (" +
		"	cat_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL," +
		"	level_0 VARCHAR(40) NOT NULL," +
		"	level_1 VARCHAR(40) NOT NULL," +
		"	level_2 VARCHAR(40));"

	doQuery(db, QUERY, null);
}

function createBizCatTable(db) {
	var QUERY = "CREATE TABLE BizCat (" +
		"	biz_id CHAR(50) NOT NULL," +
		"	cat_id INT NOT NULL);"

	doQuery(db, QUERY, null);
}