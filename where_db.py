import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="31012001Th",
    database="mydatabase1"
)
print(mydb)

mycursor = mydb.cursor()

# sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"

# mycursor.execute(sql)

sql = "SELECT * FROM customers WHERE address = %s"
val = ("Park Lane 38",)

mycursor.execute(sql,val)

myresult = mycursor.fetchall()

for r in myresult:
    print(r)