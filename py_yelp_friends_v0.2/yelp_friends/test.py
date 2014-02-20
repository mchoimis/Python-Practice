"""
First of all
Make Database in Mysql localhost
"""

import MySQLdb as server
PASSWORD = '1234'

con = server.connect('localhost', 'root', PASSWORD, 'test')
cur = con.cursor()
cur.execute("CREATE DATABASE yelp")
cur.execute("show databases")
print cur.fetchall()

cur.close()
