"""

Written by FourwingsY
Written at 2013. 12. 3.
version 0.1

"""

# -*- coding: utf-8 -*-

"""
Parse User first
"""

import MySQLdb as server
import database as db
import parser
from time import sleep

SEED_ID = "2C3F1PvMw2e5YHr9r1mSdw"
PASSWORD = '1234'

def initDB(con) :
	db.dropAllTable(con)
	db.initUserTable(con)
	db.initBizTable(con)
	db.initFriendTable(con)
	db.initReviewTable(con)


def main() :
	con = server.connect(host='localhost', user='root', passwd=PASSWORD, db='yelp')
	sleep(1)
	
	with con :
		# if you want to reset all data
		initDB(con)


		# 1. parse friends : make a user pool
		# 2. parse users : get each user's profile
		# 3. parse review and biz : parse each user's review,
		#							and reviewed business
		
		# 1. & 2.

		# For FIRST SEED
		cur = con.cursor()
		sql = "SELECT friends_num FROM User WHERE userid = \'%s\'" % SEED_ID
		cur.execute(sql)
		seed = cur.fetchone()
		if seed == None or seed[0] == -1:
			updateSeed(con, SEED_ID)
		
		# And OTHER SEED
		while True :
			cur.execute("SELECT userid FROM User WHERE friends_num = -1")
			registered_yet = cur.fetchall()

			if len(registered_yet) == 0 :
				print "No more users to insert!"
				break
			
			for user in registered_yet :
				updateSeed(con, user[0])
				
				sleep(2)

		cur.close()
	con.close()



def updateSeed(con, seed_id) :
	seed = parser.parseUserPage(seed_id)
	db.insertUserData(con, seed)

	friend_list = parser.parseFriendPage(seed_id, 0)
	filtered_list = []

	# filter friends by location
	for friend in friend_list :
		if friend['location'] == "Philadelphia, PA" :
			filtered_list.append(friend)

	# insert a simplified user data
	for friend in filtered_list :
		db.insertUserData(con, friend)
		db.insertFriendData(con, seed_id, friend['userid'])



try :
        main()
except Exception, e :
        print e
finally :
        con = server.connect(host='localhost', user='root', passwd=PASSWORD, db='yelp')
        db.printData(con, "User")
