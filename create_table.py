# Import Lib
import mysql.connector

# Connect to DB
mydb = mysql.connector.connect(
    host="127.0.0.1",       #host_port
    database="mydatabase",    #database_name
    user="root",            #user
    password="31012001Th"   #pass
    )

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)