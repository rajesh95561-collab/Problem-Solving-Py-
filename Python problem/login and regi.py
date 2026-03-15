#This project is a simple menu-driven user authentication system built in Python. It allows users to register with their name, email, and password, log in with their
# credentials, and log out. User data is stored in a dictionary where the key is the username (derived from the email) and the value is a list containing the name and
# password. A global variable tracks the currently logged-in user, ensuring proper login/logout functionality. The program runs interactively through a text-based menu
# with options for register, login, logout, and exit.

database = {}
current_user = None

def user_menu():
    print("WELCOME TO MENU PAGE")
    user_input = input(
        """
        Enter 1 for register:
        Enter 2 for login:
        Enter 3 for logout:
        Enter 4 for exit:
        """
    )
    if user_input == "1":
        reg()
    elif user_input == "2":
        login()
    elif user_input == "3":
        logout()
    elif user_input == "4":
        print("Exiting program... Goodbye!")
    else:
        print("Invalid choice, try again.")
        user_menu()

def reg():
    print("WELCOME TO REGISTER PAGE")
    name = input("Enter your name: ")
    mail = input("Enter your mail: ")
    password = input("Enter your password: ")

    username = mail.split("@")[0]
    if username in database:
        print(f"{name} is already registered")
    else:
        database[username] = [name, password]
        print("You have successfully registered")
    user_menu()

def login():
    global current_user
    print("WELCOME TO LOGIN PAGE")
    mail = input("Enter your mail: ")
    password = input("Enter your password: ")
    username = mail.split("@")[0]

    if username in database:
        if password == database[username][1]:
            current_user = username
            print(f"{username} is logged in")
        else:
            print("Wrong password")
    else:
        print(f"{username} is not registered")
    user_menu()

def logout():
    global current_user
    if current_user:
        print(f"{current_user} has successfully logged out")
        current_user = None
    else:
        print("No user is currently logged in")
    user_menu()

user_menu()