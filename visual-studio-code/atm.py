LIMIT_ATTEMPTS = 3
CORRECT_PIN = 8762
attempts = 0
repeat = True
balance = 5000000000

#pin number
while True:
    try:
        if attempts == LIMIT_ATTEMPTS:
            print("You are block")
            break
        
        pin = int(input("Enter your pin number:"))
        if pin!=CORRECT_PIN:
            attempts+=1
            print("Incorrect pin number. You have ", LIMIT_ATTEMPTS-attempts, "attempts left")
            continue
        else:
            break
    except:
        print("Enter digits only")
        

#menu      
while True:
    try:
        print("Menu\n============")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = int(input("Choice:"))
        if choice < 1 or choice > 4:
            print("Invalid choice!")
            continue
        
        if choice == 1:
            print("Your current balance is ", balance)
        elif choice == 2:
            amount = int(input("Amount to deposit:"))
            if amount <=0:
                raise ArithmeticError("Amount must be a positive number or greater than 0")
            balance = amount + balance
            print("money successful deposit. Your new balance is", balance)
        elif choice == 3:
            amount = int(input("Amount to withdraw:"))
            if amount > balance:
                raise ArithmeticError("You cannot draw more than you have!!")
            balance = balance - amount
            print("Money successful withdraw. New balance is: ", balance)
            
            
            
    except ValueError as e:
        print(e)
        #print("Invalid input. Please enter number only!")
    except ArithmeticError as e:
        print(e)
        #print("Invalid amount trying to deposit or withdraw")
    except:
        print("An error prevent our system from perform the operation. Please try again later")