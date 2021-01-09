import mysql.connector as myconc
sq=myconc.connect(host='localhost',user='root',password="rithul",database="codeesa")
if sq.is_connected():
    print("connected")
sqc=sq.cursor()