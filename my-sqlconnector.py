#code to connect mySQL and Python
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='toor99',
    port='3306',
    database='banking_system_db'
)
mycursor = mydb.cursor()
mycursor.execute('select * from banking_system_users')
users = mycursor.fetchall()

#this allows me to see my database
for user in users:
    print(user)



