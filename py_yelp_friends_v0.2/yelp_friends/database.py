"""

Written by FourwingsY
Written at 2013. 12. 3.
version 0.1

"""

# -*- coding: utf-8 -*-

# import MySQLdb as db

"""
connection-required functions

init- : create DB table
insert- : insert record into table
get- : return data from table

"""
def dropAllTable(con) :
	with con :
		cur = con.cursor()
		cur.execute( "DROP TABLE IF EXISTS Friend" )
		cur.execute( "DROP TABLE IF EXISTS Review" )
		cur.execute( "DROP TABLE IF EXISTS Biz" )
		cur.execute( "DROP TABLE IF EXISTS User" )
		cur.close()

def initUserTable(con) :
	with con :
		cur = con.cursor()
		cur.execute(
		"""
			CREATE TABLE User (
				userid CHAR(22) PRIMARY KEY NOT NULL,
				name VARCHAR(30) NOT NULL,
				location VARCHAR(30) NOT NULL,
				since VARCHAR(15),
				friends_num INT NOT NULL DEFAULT -1,
				reviews_num INT NOT NULL DEFAULT -1,
				firsts_num INT,
				elite VARCHAR(30),
				votes VARCHAR(20),
				complements INT,
				updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
			)"""
		);
		cur.close()

def initBizTable(con) :
	with con :
		cur = con.cursor()
		cur.execute(
		"""
			CREATE TABLE Biz (
				biz_url CHAR(50) PRIMARY KEY NOT NULL,
				name VARCHAR(50) NOT NULL,
				total_rating FLOAT NOT NULL,
				review_count INT NOT NULL,
				category VARCHAR(50) NOT NULL,
				address VARCHAR(100) NOT NULL,
				price VARCHAR(5),
				updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
			)"""
		);
		cur.close()

def initReviewTable(con) :
	with con :
		cur = con.cursor()
		cur.execute(
		"""
			CREATE TABLE Review (
				writerid CHAR(22) NOT NULL,
				biz_url CHAR(50) NOT NULL,
				rating FLOAT NOT NULL,
				post_date DATE NOT NULL,
				review TEXT,
				FOREIGN KEY (writerid)
					REFERENCES User(userid)
					ON UPDATE CASCADE ON DELETE RESTRICT,
				FOREIGN KEY (biz_url)
					REFERENCES Biz(biz_url)
					ON UPDATE CASCADE ON DELETE RESTRICT
			)"""
		);
		cur.close()

def initFriendTable(con) :
	with con :
		cur = con.cursor()
		cur.execute(
		"""
			CREATE TABLE Friend (
				userid CHAR(22) NOT NULL,
				friendid CHAR(22) NOT NULL,
				FOREIGN KEY (userid)
					REFERENCES User(userid)
					ON UPDATE CASCADE ON DELETE RESTRICT,
				FOREIGN KEY (friendid)
					REFERENCES User(userid)
					ON UPDATE CASCADE ON DELETE RESTRICT
			)"""
		);
		cur.close()

def insertUserData(con, user) :

	# MAKE MULTI-DATA TO SINGLE-STRING
	votes = None
	elite = None

	try :
		votes = user['votes']
	except KeyError :
		pass
	try :
		elite = user['elite']
	except KeyError :
		pass
	
	if votes != None :
		user['votes'] = handleVoteInfo(votes)
	if elite != None :
		user['elite'] = handleEliteInfo(elite)

	with con :
		cur = con.cursor()
		QUERY = makeInsertQuery("User", user)
		if QUERY != None :
			cur.execute(QUERY)
		cur.close()


def insertBizData(con, biz) :

	category = biz['category']
	biz['category'] = handleCategoryInfo(category)

	with con :
		cur = con.cursor()
		QUERY = makeInsertQuery("Biz", biz)
		if QUERY != None :
			cur.execute(QUERY)
		cur.close()

def insertReviewData(con, review) :

	post_date = review['post_date']
	review['post_date'] = handleDate(post_date)

	text = review['review']
	review['review'] = text[5:-4]

	with con :
		cur = con.cursor()
		QUERY = makeInsertQuery("Review", review)
		if QUERY != None :
			cur.execute(QUERY)
		cur.close()

def insertFriendData(con, userid, friendid) :

	with con :
		cur = con.cursor()

		friend = {'userid':userid, 'friendid':friendid}
		QUERY = makeInsertQuery("Friend", friend)
		if QUERY != None :
			cur.execute(QUERY)

		cur.close()


def getAllData(con, table_name) :
	with con :
		cur = con.cursor()
		cur.execute("SELECT * FROM " + table_name)
	return cur.fetchall()

"""
IMPORTANT
making query function

"""
def makeInsertQuery(table_name, data) :
	# ORDERING DATA
	query_column = []
	query_value = []
	p_key = getPrimaryKeys(table_name)

	for key in data.keys() :
		value = data[key]
		value = handleApostrophe(value)
		query_column.append(key)
		query_value.append(value)
	
	column_count = len(query_column)

	# MAKE QUERY
	try :
		QUERY = "INSERT INTO " + table_name + " ("
		for i in range(0, column_count) :
			QUERY += query_column[i] + ', '
		QUERY = QUERY[:-2] + ") "

		QUERY += "VALUES ("
		for i in range(0, column_count) :
			QUERY += "'" + query_value[i].encode('utf-8') + "', "
		QUERY = QUERY[:-2] + ") ON DUPLICATE KEY UPDATE "
		
		for i in range(0, column_count) :
			QUERY += query_column[i] + "='" + query_value[i].encode('utf-8') + "', "

	except UnicodeError :
		print "Unicode Error at "
		print data
		return None

	# print QUERY[:-2]
	return QUERY[:-2]

def getPrimaryKeys(table_name) :

	if table_name == "User" :
		return ["userid"]
	elif table_name == "Biz" :
		return ["biz_url"]
	elif table_name == "Review" :
		return ["writerid", "biz_url"]
	elif table_name == "Friend" :
		return ["userid", "friendid"]

"""
make unsuitable parsed data database-suitable

"""
def handleApostrophe(string) :
	splited = string.split("'")
	edited = "\\'".join(splited)
	return edited

def handleVoteInfo(votes) :
	# {'votes':{'funny':'123', 'useful':'52', 'cool':'156'} }
	# -> '123-52-156'
	vote_info = [votes['funny'], votes['useful'], votes['cool']]

	return '-'.join(vote_info)

def handleEliteInfo(elite) :
	# ['2013', '2012', '2011', '2010']
	# -> '13-12-11-10'
	years = []
	for year in elite :
		years.append(year[-2:])
		
	return '-'.join(years)

def handleCategoryInfo(category) :
	# [['Restaurants', 'Italian'], ['Restaurants', 'Japanese']]
	# -> 'Restaurants-Italian||Restaurants-Japanese'
	cats = []
	for subcat in category :
		cats.append('-'.join(subcat))
	return '||'.join(cats)

def handleDate(post_date) :
	# '8/12/2013' -> '2013-8-12'
	splited = post_date.split('/')
	rearranged = splited[-1:] + splited[:-1]
	return '-'.join(rearranged)

"""
from DB to txt file

"""
def printData(con, table_name) :
	with con :
		cur = con.cursor()
		cur.execute( "SELECT * FROM " + table_name )
		result = cur.fetchall()
		cur.close()

	f = open("User.txt", "w+")
	for record in result :
		f.write(str(record))
		f.write('\n')
