import database
conn = database.connect()
print("Welcome to passwords manager!")
while True:
    print("1. Create profile.\n2. Login to existing profile" \
    "\n3. Update master password of existing profile.\n4. Forgot Password" \
    "\n5. Exit passwords manager.")
    choice = int(input("Please enter your choice from 1,2,3 or 4: "))
    if choice==1:
        database.createProfile()
        print("")
    elif choice==2:
        database.loginProfile()
        print("")
    elif choice==3:
        database.updatePassword()
        print("")
    elif choice==5:
        print("")
        print("Thank you for using passwords manager!")
        break
    else:
        print("Invalid choice! Please try again.")
