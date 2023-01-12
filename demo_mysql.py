# Import Lib
import mysql.connector

# Connect to DB
mydb = mysql.connector.connect(
    host="127.0.0.1",       #host_port
    user="root",            #user
    password="31012001Th"   #pass
    )

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")