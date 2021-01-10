import mysql.connector as myconc


def databaseexistcheck(name):
    sq = myconc.connect(host='localhost', user='root',
                        password="bezlin2003")
    if sq.is_connected():
        cursor = sq.cursor()
        cursor.execute(cursor.execute("SHOW DATABASES LIKE '{}'".format(name)))
        datas = cursor.fetchall()
        if len(datas) < 1:
            return False
        else:
            return True


def tableexistcheck(name):
    sq = myconc.connect(host='localhost', user='root',
                        password="bezlin2003")
    if sq.is_connected():
        cursor = sq.cursor()
        cursor.execute(cursor.execute("SHOW TABLES LIKE '{}'".format(name)))
        datas = cursor.fetchall()
        if len(datas) < 1:
            return False
        else:
            return True
