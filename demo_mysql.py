# Import Lib
import mysql.connector

# Connect to DB
mydb = mysql.connector.connect(
    host="127.0.0.1",       #host_port
    database="new_db_1",    #database_name
    user="root",            #user
    password="31012001Th"   #pass
    )
print(mydb)