import mysql.connector as myconc
sq = myconc.connect(host='localhost', user='root',
                    password="bezlin2003")
if sq.is_connected():
    print("connected")
sqc = sq.cursor()
