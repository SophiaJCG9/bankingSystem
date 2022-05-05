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

#access userNames in databases
myCursor.execute("SELECT userName FROM bs_database")
databaseUser = myCursor.fetchall()
#This makes my userNameList accesible
userNameList = [user[0] for user in databaseUser]

#check if they are an admin or a customer with userRole variable
myCursor.execute("SELECT userType FROM bs_database")
userRole = myCursor.fetchall()
#This makes the userRole list accesible
userRoleList = [user[0] for user in userRole]


#access pins in database
myCursor.execute("SELECT userPin FROM bs_database")
databasePin = myCursor.fetchall()
#This makes my pins accessible.
pinList = [pin[0] for pin in databasePin]

#This is my Welcome Page.
print("=======Hello User! Welcome to the Banking System UI.=======")
userType = input("Please Enter Whether You Are an Admin or Customer: ")

#check if userName and Pin are correct. Check if userName is actually a customer.
if userType == "Admin":
    print("\n=======Hello Admin. Please enter your Username and Pin.=======")
    #stores the inputted user name
    adminUserName = input("UserName: ")
    #checks if the input is in the database
    if adminUserName in userNameList:
        #stores the correct username
        correctUN = adminUserName
        #stores the user name index for later comparison with pin and admin index.
        UNindex = userNameList.index(correctUN)
        #stores if the user at the specified index is a customer or admin
        userRole_at_index = (userRoleList[UNindex])
        #checks if the user is an Admin
        if userRole_at_index == "Admin":
            pin = input("Pin: ")
            #checks if pin in pinlist
            if pin in pinList:
                # stores the correct pin
                correctPin = pin
                # stores the pin index
                pinIndex = pinList.index(correctPin)
                print("The Pin Index is: ", pinIndex)
                # if the pin index is in the same index as the UN, then they entered the correct pin for their corressponding userName.
                if pinIndex == UNindex:
                    print("\n=======You have succesfully entered the Admin Page.")
                else:
                        print("\nSorry the pin you have entered is incorrect. Try Again.")
        #If user is not an admin
        else:
            print("Sorry. You are not authorized to enter the Admin page.")


    #Need to add code that has them enter the pin again.
    #Add Code: Tells user that they must contact their admin to create an account.
    else:
        print("\nSorry. Your User Name is not in the database. ")


elif userType == "Customer":
    print("\n=======Hello Customer. Please enter your Username and Pin.=======")
    customUserName = input("UserName: ")
    if customUserName in userNameList:
        #stores the correct username
        correctUN = customUserName
        #stores the user name index for later comparison with pin.
        UNindex = userNameList.index(correctUN)
        print("The UN Index is: ", UNindex)
        # stores if the user at the specified index is a customer or admin
        userRole_at_index = (userRoleList[UNindex])
        #checks if pin in pinlist
        if userRole_at_index == "Customer":
            pin = input("Pin: ")
            #checks if pin in pinlist
            if pin in pinList:
                # stores the correct pin
                correctPin = pin
                # stores the pin index
                pinIndex = pinList.index(correctPin)
                print("The Pin Index is: ", pinIndex)
                # if the pin index is in the same index as the UN, then they entered the correct pin for their corressponding userName.
                if pinIndex == UNindex:
                    print("\n=======You have succesfully entered the Customer Page.")
                else:
                    print("\nSorry the pin you have entered is incorrect. Try Again.")
        #If user is not an admin
        else:
            print("Sorry. You are not authorized to enter the Customer page. Contact your Admin to create an account.")


