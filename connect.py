import mysql.connector as myconc
sq = myconc.connect(host='localhost', user='root',
                    password="bezlin2003")


def databaseexistcheck(name):
    if sq.is_connected():
        cursor = sq.cursor()
        cursor.execute(cursor.execute("SHOW DATABASES LIKE '{}'".format(name)))
        datas = cursor.fetchall()
        if len(datas) < 1:
            return False
        else:
            return True


def tableexistcheck(name, database):

    if sq.is_connected():
        cursor = sq.cursor()
        cursor.execute(cursor.execute("use "+database))
        cursor.execute(cursor.execute("SHOW TABLES LIKE '{}'".format(name)))
        datas = cursor.fetchall()
        if len(datas) < 1:
            return False
        else:
            return True


def createdatabase(name):
    if sq.is_connected():
        cursor = sq.cursor()
        cursor.execute(cursor.execute("CREATE DATABASE "+name))


# def createtable(name, database):
#     if sq.is_connected():
#         cursor = sq.cursor()
#         cursor.execute(cursor.execute("CREATE DATABASE "+name))
