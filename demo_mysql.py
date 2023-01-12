# Import Lib
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    database="new_db_1",
    user="root",
    password="31012001Th"
    )
print(mydb)