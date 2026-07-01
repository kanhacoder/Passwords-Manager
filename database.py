import mysql.connector

def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234", 
            database="passwordsDB"
        )

        return connection

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

def createProfile():
    username = input("Enter a username: ")
    while True:
        master_passwordi = input("Enter master_password: ")
        master_passwordc = input("Enter master_password again: ")
        if master_passwordc!=master_passwordi:
            print("Password entered again does not match initial password\nPlease try again.")
        else:
            print("Profile created successfully!")
            break
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO PROFILE_ID(USERNAME,MASTER_PASSWORD) VALUES(%s,%s)",(username,master_passwordc,))
    conn.commit()
    cursor.close()
    conn.close()

def addAccount(pid):
    platform = input("Enter the platform of the account to be stored: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords(profile_id,website,username,password) VALUES(%s,%s,%s,%s)",(pid,platform,username,password,))
    conn.commit()
    cursor.close()
    conn.close()

def viewAccount(pid):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT website FROM passwords WHERE profile_id=%s",(pid,))
    records = cursor.fetchall()
    print("\nStored Accounts' platforms: ")
    for i in records:
        print(i[0])
    cursor.close()
    conn.close()

def viewPassword(pid):
    conn = connect()
    cursor = conn.cursor()
    while True:
        platform = input("Enter the platform whose account details are to be viewed: ")
        cursor.execute("SELECT username,password FROM PASSWORDS WHERE website=%s AND profile_id=%s",(platform,pid,))
        record = cursor.fetchone()
        if record is None:
            print("Invalid platform!\nPlease try again.")
        else:
            print("")
            print("Platform:",platform,"\nUsername:",record[0],"\nPassword:",record[1])
            break
    cursor.close()
    conn.close()

def updatePassword(pid):
    conn = connect()
    cursor = conn.cursor()
    while True:
        platform = input("Enter platform of account whose password is to be updated: ")
        cursor.execute("SELECT username,password FROM passwords WHERE website=%s AND profile_id=%s",(platform,pid,))
        record = cursor.fetchone()
        if record is None:
            print("No stored account found for entered platform.\nPlease try again.")
        else:
            username = input("Enter new username(Enter original username if unchanged): ")
            password = input("Enter new password(Enter original password if unchanged): ")
            cursor.execute("UPDATE passwords SET username=%s,password=%s WHERE website=%s AND profile_id=%s",(username,password,platform,pid,))
            break
    conn.commit()
    cursor.close()
    conn.close()

def deleteAccount(pid):
    conn = connect()
    cursor = conn.cursor()
    while True:
        platform = input("Enter platform whose account data is to be deleted: ")
        username = input(f"Enter username for your account on {platform}: ")
        cursor.execute("SELECT * FROM passwords WHERE website=%s AND username=%s AND profile_id=%s",(platform,username,pid,))
        record = cursor.fetchone()
        if record is None:
            print("Invalid platform or username entered!\nPlease try again.")
        else:
            cursor.execute("DELETE FROM passwords WHERE website=%s AND username=%s AND profile_id=%s",(platform,username,pid,))
            print("Record successfully deleted!")
            break
    conn.commit()
    cursor.close()
    conn.close()


def loginProfile():
    conn = connect()
    cursor = conn.cursor()
    username = input("Enter your username: ")
    cursor.execute("SELECT profile_id,master_password FROM PROFILE_ID WHERE username=%s",(username,))
    record = cursor.fetchone()
    if record is None:
        print("Invalid Username!\nPlease try again.")
    else:
        pid = record[0]
        paswd = record[1]
        while True:
            password = input("Enter master_password: ")
            if paswd == password:
                print("Successfully logged in!")
                print(f"\nWelcome {username}!")
                while True:
                    print("1. Add an account.")
                    print("2. View password for a stored account.")
                    print("3. Update password of a stored account.")
                    print("4. Delete a stored account.")
                    print("5. View stored account.")
                    print("6. Log out of this account.")
                    choice = int(input("Enter your choice from 1,2,3,4 or 5: "))
                    if choice==1:
                        addAccount(pid)
                    elif choice==2:
                        viewPassword(pid)
                    elif choice==3:
                        updatePassword(pid)
                    elif choice==4:
                        deleteAccount(pid)
                    elif choice==5:
                        viewAccount(pid)
                    elif choice==6:
                        cursor.close()
                        conn.close() 
                        print("Thank you for using Passwords Manager!")
                        return
                    else:
                        print("Invalid choice!\nPlease try again.")
            else:
                cursor.close()
                conn.close()                
                print("Invalid password entered.")
                break

def updatePassword():
    conn = connect()
    cursor = conn.cursor()
    while True:
        username = input("Enter your username: ")
        password = input("Enter your account password: ")
        cursor.execute("SELECT master_password FROM master_user WHERE username=%s",(username,))
        record = cursor.fetchone()
        if record is not None:
            if password==record[0]:
                while True:
                    new_password = input("Enter new password: ")
                    confirm_newpassword = input("Re-enter new password: ")
                    if new_password==confirm_newpassword:
                        cursor.execute("UPDATE master_user SET master_password=%s WHERE username=%s",(confirm_newpassword,username,))
                        print("Password updated successfully!")
                        break
                    else:
                        print("Entered passwords don't match!\nPlease try again.")
                break
            else:
                    print("Invalid username or password entered!\nPlease try again.")
        else:
            print("Account with the given credentials does not exist!\nPlease try again.")
    conn.commit()
    cursor.close()
    conn.close()

def forgotPassword():
    conn = connect()
    cursor = conn.cursor()
    while True:
        username = input("Enter username of your account: ")
        cursor.execute("SELECT * FROM master_user WHERE username=%s",(username,))
        record = cursor.fetchone()
        if record is not None:
            securityanswer = input(record[3]+" : ")
            if securityanswer.strip().lower()==record[4].strip().lower():
                newpassword = input("Enter new password: ")
                confirmpassword = input("Re-enter new password: ")
                if newpassword==confirmpassword:
                    if newpassword==record[2]:
                        print("New password cannot be same as current password.\nPlease try again.")
                    else:
                        cursor.execute("UPDATE master_user SET master_password=%s WHERE username=%s",(newpassword,username,))
                        print("Password updated successfully!")
                        break
                else:
                    print("New password should match Re-entered password.\nPlease try again.")
            else:
                print("Your answer to the security question is incorrect.\nPlease try again.")
        else:
            print("Account with entered username does not exist.\nPlease try again.")
    conn.commit()
    cursor.close()
    conn.close()