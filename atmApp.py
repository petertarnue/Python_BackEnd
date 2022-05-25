name = input("what is your name? \n")

allowedUsers = ["peter", "Kollie", "Eve", "Kebbeh", "Joseph", "Wolliyean", "Peter"]
allowedPassword = ['passpeter', 'passkollie', 'evelyn',
                   'kb','jojo', 'wolli', 'petiano']

if name in allowedUsers:
    password = input("enter your password \n")
    userId = allowedUsers.index(name)

    if password == allowedPassword[userId]:
        print("welcome %s" % name)
        print("These are the options available")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")
        
        selectedOption = int(input("please select an option:"))
        print(selectedOption == 1)
        
        if(selectedOption == 1):
            print("you selected %s" % selectedOption) 
            
        elif(selectedOption == 2):
            print("you selected %s" % selectedOption)
            
        elif(selectedOption == 3):
            print("you selected %s" % selectedOption)
            
        else:
            print("Invalid Option selected, please try again")
        
    else:
        print("Password Incorrect, please try again")
else:
    print("Name not found, please try again")
 

