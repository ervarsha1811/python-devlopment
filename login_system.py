def login():
    # Correct username and password
    correct_username = "admin"
    correct_password = "python123"

    # Starting attempts
    attempts = 0

    # Maximum 3 attempts
    while attempts < 3:

        # Take username and password from user
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check username and password
        if username == correct_username and password == correct_password:
            print("Login successful!")
            break

        else:
            # Increase attempts by 1
            attempts += 1

            print("Incorrect username or password.")

            # Show remaining attempts
            print("Attempts remaining:", 3 - attempts)

    # If all 3 attempts are wrong
    if attempts == 3:
        print("Account locked!")


# Call the function
login()