import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "31012001Th",
    database = "mydatabase1"
)
print(mydb)

mycursor = mydb.cursor()

sql = "select * from customers order by name desc"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for r in myresult:
    print(r)