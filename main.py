#code to connect mySQL and Python
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='toor99',
    port='3306',
    database='banking_system_db'
)

#allows me to view my database while coding
myCursor = mydb.cursor()
myCursor.execute('select * from bs_database')
dataBase = myCursor.fetchall()

for x in dataBase:
    print(x)

#see userName in databases while coding
myCursor.execute("SELECT userName FROM bs_database")
databaseUser = myCursor.fetchall()
#This makes my userNameList accesible
userNameList = [user[0] for user in databaseUser]

#access pins in database
myCursor.execute("SELECT userPin FROM bs_database")
databasePin = myCursor.fetchall()
#This makes my pw's accessible.
pinList = [pin[0] for pin in databasePin]

#list to match corresponding userName with pin.


#This is my Welcome Page.
print("=======Hello User! Welcome to the Banking System UI.=======")
userType = input("Please Enter Whether You Are an Admin or Customer: ")

#check userName and Pin
if userType == "Admin":
    print("\n=======Hello Admin. Please enter your Username and Pin.=======")
    adminUserName = input("UserName: ")
    if adminUserName in userNameList:
        correctUN = adminUserName
        UNindex = userNameList.index(correctUN)
        print("The UN Index is: ", UNindex)
        pin = input("Pin: ")
        if pin in pinList:
            correctPin = pin
            pinIndex = pinList.index(correctPin)
            print("The Pin Index is: ", pinIndex)
            if pinIndex == UNindex:
                print("\n=======You have succesfully entered the Admin Page.")
            else:
                print("\nSorry the pin you have entered is incorrect. Try Again.")
    else:
        print("\nSorry. Your User Name is not in the database. ")

elif userType == "Customer":
    print("\n=======Hello Customer. Please enter your Username and Pin.=======")
    customUserName = input("UserName: ")
    pin = input("Pin: ")




