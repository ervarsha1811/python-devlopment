def  atm():
    # Starting balance
    balance = 10000

    # Menu will keep showing until Exit is selected
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        # Check current balance
        if choice == 1:
            print("Your balance is: ₹", balance)

        # Deposit money
        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print("Amount deposited successfully!")
            print("Updated balance: ₹", balance)

        # Withdraw money
        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))

            # Check if enough balance is available
            if amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Updated balance: ₹", balance)
            else:
                print("Insufficient balance!")

        # Exit the ATM
        elif choice == 4:
            print("Thank you for using the ATM!")
            break

        # If user enters a wrong choice
        else:
            print("Invalid choice! Please try again.")


# Call the ATM function
atm()