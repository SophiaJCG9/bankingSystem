import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='toor99',
    port='3306',
    database='banking_system_users'
)
mycursor = mydb.cursor()
mycursor.execute('select * from banking_system_users')

users = mycursor.fetchall()

for user in users:
    print(user)
    print('username', + user[1])
    print('username', + user[2])



