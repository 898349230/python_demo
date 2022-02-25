#coding=utf-8

import MySQLdb
con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mysql')
cursor =con.cursor()
sql ="select * from user limit 10"
cursor.execute(sql)

row=cursor.fetchone()
print (row)
cursor.close()
con.close()

