import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "passwd", database = "Alendb")

mycursor = mydb.cursor()

mycursor.execute("select * from moviest")

result = mycursor.fetchall()

print(result)


