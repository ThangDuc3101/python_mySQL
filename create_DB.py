# Import Lib
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="31012001Th"
    )

mycursor = mydb.cursor()

# Excute query
mycursor.execute("CREATE DATABASE mydatabase1")

#Check databases in MySQL
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)




