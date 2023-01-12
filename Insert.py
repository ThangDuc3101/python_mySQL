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

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")