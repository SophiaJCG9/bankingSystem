#library to make changes to database
import mysql.connector
#code to connect mySQL and Python
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='toor99',
    port='3306',
    database='banking_system_db'
)
myCursor = mydb.cursor()

#allows me to view my database while coding
myCursor.execute('select * from bs_database')
dataBase = myCursor.fetchall()
print("This is the banking system database: ")
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

#fetch the balance for the customers
myCursor.execute("SELECT balance FROM bs_database")
customerBalance = myCursor.fetchall()
#This makes my balanceList accesible
balanceList = [user[0] for user in customerBalance]

#access pins in database
myCursor.execute("SELECT userPin FROM bs_database")
databasePin = myCursor.fetchall()
#This makes my pins accessible.
pinList = [pin[0] for pin in databasePin]

#access pins in database
myCursor.execute("SELECT userID FROM bs_database")
databaseID = myCursor.fetchall()
#This makes my pins accessible.
userIDList = [ID[0] for ID in databaseID]

#This is my Welcome Page.
print("=======Hello User! Welcome to the Banking System UI.=======")
#This segment checks the userType and then if their input was valid.
userType = input("\nEnter whether you are an Admin or Customer. By entering \n - The number 1 for Admin \n - The number 2 for Customer \nPlease enter 1 or 2: ")

#while loop checks if userName and Pin are correct. While they are not, asks for username or pin again.
while True:
    if userType == "1":#This is the Admin route since 1 indicates Admin.
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
                    #stores the correct pin
                    correctPin = pin
                    # stores the pin index
                    pinIndex = pinList.index(correctPin)
                    # if the pin index is in the same index as the UN, then they entered the correct pin for their corressponding userName.
                    if pinIndex == UNindex:
                        print("\n=======You have succesfully entered the Admin Page.")
                        print("Your options are \n- 1: Create Account \n- 2: Delete Account \n- 3: Modify Account")
                        userInput = input("\nPlease enter what action you wish to take by inputting 1, 2, or 3: ")
                        break
                    else:
                            print("\nSorry the pin you have entered is incorrect. Try Again.")
            #If enters the else statment then the user is not an admin
            else:
                print("Sorry. You are not authorized to enter the Admin page.")
        else:
            #if enters this else statement then their username does not exist at all
            print("\nSorry. Your User Name is not in the database. ")
    elif userType == "2":#2 indicates the user is a customer.
        print("\n=======Hello Customer. Please enter your Username and Pin.=======")
        customUserName = input("UserName: ")
        if customUserName in userNameList:
            #stores the correct username
            correctUN = customUserName
            #stores the user name index for later comparison with pin.
            UNindex = userNameList.index(correctUN)
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
                    # if the pin index is in the same index as the UN, then they entered the correct pin for their corressponding userName.
                    if pinIndex == UNindex:
                        print("\n=======You have succesfully entered the Customer Page.")
                        print("Your options are \n- 1: Check Balance \n- 2: Withdraw from balance \n- 3: Deposit into balance")
                        userInput = input("\nPlease enter what action you wish to take by inputting 1, 2, or 3: ")
                        print(userInput)
                        break
                    else:
                        print("\nSorry the pin you have entered is incorrect. Try Again.")
            #If user is not an admin
            else:
                print("Sorry. You are not authorized to enter the Customer page. Contact your Admin to create an account.")

#lets user perform tasks while they wish to continue
while True:
    #lets user view their balance
    def checkBalance():
        userBalance = (balanceList[UNindex])
        if userInput == "1":
            print("Your check balance is: ", userBalance)

    #lets user withdraw from balance
    def withdraw():
        userBalance = (balanceList[UNindex])
        userBalanceNum = int(userBalance)
        print(userBalanceNum)
        if userInput == "2":
            print("Your check balance is: ", userBalance)
            withdraw_amt = int(input("\nHow much would you like to withdraw from your balance: "))
            newUserBalance = userBalanceNum - withdraw_amt

            # Alter in the database
            query = ("Update bs_database set balance = %s where userPIN = %s")
            # pass in the new balance and the users ID
            tuple1 = (newUserBalance, correctPin)
            myCursor.execute(query, tuple1)
            mydb.commit()
            print("Your previous balance was: ", userBalance, ". Your new balance is: ", newUserBalance)

            # update value in balance list
            balanceList[UNindex] = newUserBalance



    #lets user deposit from balance
    def deposit():
        userBalance = (balanceList[UNindex])
        userBalanceNum = int(userBalance)
        if userInput == "3":
            print("Your check balance is: ", userBalance)
            depositAmt = int(input("\nHow much would you to deposit into your account: "))
            newUserBalance = userBalanceNum + depositAmt
            print("Your previous balance was: ",userBalance, ". Your new balance is: ", newUserBalance)

            # Alter in the database
            query = ("Update bs_database set balance = %s where userPIN = %s")
            # pass in the new balance and the users ID
            tuple1 = (newUserBalance, correctPin)
            myCursor.execute(query, tuple1)
            mydb.commit()
            print("Your previous balance was: ", userBalance, ". Your new balance is: ", newUserBalance)
            # update value in balance list
            balanceList[UNindex] = newUserBalance


    #if the userType is 2 then they are a customer
    if userType == "2":#call all my customer functions
        checkBalance()
        withdraw()
        deposit()
        userContinue = input("\nWould you like to make other changes? Please input 1 for Yes or 2 for No: ")
        if userContinue == "1":
            print("Your options are \n- 1: Check Balance \n- 2: Withdraw from balance \n- 3: Deposit into balance")
            userInput = input("\nPlease enter what action you wish to take by inputting 1, 2, or 3: ")
            continue
        print("======Thanks for using the banking system UI.======")
        break
    #The Admin Functions
    def createAcc():
        if userInput == "1":
            role = input("Is this new account for an admin or customer? Please input \n - 1: Admin or \n - 2: Customer: \nInput 1 or 2: ")
            #appends cutomer or admin depending on the role the user inputted
            if role == "1":
                newUserRole = ("Admin")
                userRoleList.append(newUserRole)
                print(userRoleList)
                #if the user is an admin then they should not have a balance
                newBalanceVal = None
            else:
                newUserRole = ("Customer")
                userRoleList.append(newUserRole)
                print(userRoleList)
                # stores the balance for this customer
                newCustBal = input("Please enter the balance for this user: ")
                balanceList.append(newCustBal)
                newBalanceVal = (newCustBal)

            # the new userID is stored in the list
            newUserID = int(input("Enter a one digit ID Number: "))
            userIDList.append(newUserID)
            #the new username is stored in the list
            newUserName = input("Enter the user name of the account you wish to add: ")
            userNameList.append(newUserName)
            #the new userPIN is stored in the list
            newUserPin = input("Enter a four digit pin for the new user name: ")
            pinList.append(newUserPin)
            #insert new admin or customer into my database with all new values
            newUser = "INSERT INTO bs_database (userID, userType, userName, userPin, balance) VALUES (%s, %s, %s, %s, %s)"
            newVals = (newUserID, newUserRole, newUserName, newUserPin, newBalanceVal)
            myCursor.execute(newUser, newVals)
            mydb.commit()
            print("Your new user was succesfully created and added to the database.")
    def deleteAcc():
        if userInput == "2":
            #Gets the userName they wish to delete.
            print("---------------------------------------")
            deleteUserName = input("\nPlease enter the user name of the account you wish to delete: ")
            while deleteUserName not in userNameList:
                print("Sorry. This username is not in the database. Please Try again: ")
                print("----------------------------------")
                deleteUserName = input("\nPlease enter the user name of the account you wish to delete: ")
            #Makes sure they have the pin to co
            print("---------------------------------------")
            deletePin = input("Please enter your ADMIN PW to confirm deletion of account: ")
            if deletePin == pinList.index[correctPin]:
                # Confirms deletion of account
                print("---------------------------------------")
                userConfirmation = input("Are you sure you wish to delete the user with this username: Please enter 1 for YES or 2 for NO.")
            else:
                while deletePin != pinList.index[correctPin]:
                    deletePin = input("That pin was incorrect. Please enter your ADMIN PW again to confirm deletion of account: ")
            if userConfirmation == "1":
                #Deletes the values from the database
                deleted_values = (deleteUserName, deletePin)
                delUser = ("DELETE FROM bs_database WHERE userName = (%s) and userPin = (%s)")
                myCursor.execute(delUser, deleted_values)
                mydb.commit()
                print("---------------------------------------")
                print("The account was succesfully deleted.")
            else:
                print("---------------------------------------")
                print("Understood. Will not delete account.")
    def modifyAcc():
        if userInput == "3":
            print("You will have the oppurtunity to change the username or password. If you do not wish to change the userName or password simply type 2. This will make no changes.")
            #The userID is stored
            userID = input("\nPlease enter the userID of the account you wish to modify: ")
            if userID not in userIDList:
                print(userIDList)
                print("Sorry. This userID is not in the database please try again.")
                print("---------------------------------------")
                userID = input("\nPlease enter the userID of the account you wish to modify: ")
            #Checks if they wish to change the userName
            change = input("\nDo you wish to change the userName? Please enter 1 for yes and 2 for no:  ")
            if change == "1":#if yes, then changes the userName
                changeUN = input("\nPlease enter the new user name: ")
                updateUN = ("Update bs_database set userName = %s where userID = %s")
                # pass in the new userName
                newUN = (changeUN, userID)
                myCursor.execute(updateUN, newUN)
                mydb.commit()
            else:#User does not wish to change userName
                print("Ok. The user name will not be changed.")
            #Checks if they wish to make another change for the password
            nextChange = input("\nDo you wish to change the password for the corresponding userName. Please enter 1 for yes and 2 for no: ")
            if nextChange == "1":#If yes, then they can change the pw
                changePW = input("\nPlease enter the new password: ")
                updatePW = ("Update bs_database set userPin = %s where userID = %s")
                # pass in the new password
                newPW = (changePW, userID)
                myCursor.execute(updatePW, newPW)
                mydb.commit()
            else:#They did not wish to change pw.
                print("\nOk. The user name will not be changed.")
            if change == "1":#Then they made some changes so the following should be printed.
                print("\nYou have now succesfully modified an account.")
            elif nextChange == "1":
                print("\nYou have now succesfully modified an account.")
    if userType == "1":#1 indicates they are an admin
        #call all my admin functions.
        createAcc()
        deleteAcc()
        modifyAcc()
        #checks if they wish to make other changes.
        userContinue = input("\nWould you like to make other changes? Please input 1 for Yes or 2 for No: ")
        if userContinue == "1":
            print("Your options are \n- 1: Create Account \n- 2: Delete Account \n- 3: Modify Account")
            userInput = input("\nPlease enter what action you wish to take by inputting 1, 2, or 3: ")
            continue
        print("======Thanks for using the banking system UI.======")
        break





