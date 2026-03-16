class Atm:
    """
    ATM Simulation Class:
    Provides a simple ATM interface with features to create a PIN,
    deposit money, withdraw funds, and check balance. Uses console
    input/output for user interaction and maintains account state.
    """

    def __init__(self):
        """Initialize ATM with empty PIN and zero balance."""
        self.pin = ""
        self.balance = 0

    def menu(self):
        """Display menu and handle user choices until exit."""
        while True:
            user_input = input("""
            Hello, how would you like to proceed?
            1. Create PIN
            2. Deposit
            3. Withdraw
            4. Check Balance
            5. Exit
            """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_funds()
            elif user_input == "5":
                print("Thank you for using SBI ATM. Goodbye!")
                break
            else:
                print("Invalid input, please try again.")

    def create_pin(self):
        """Allow user to set a new PIN."""
        self.pin = input("Enter new PIN number: ")
        print("PIN updated successfully.")

    def deposit(self):
        """Deposit money after verifying PIN."""
        temp = input("Enter your PIN number: ")
        if temp == self.pin:
            try:
                amount = int(input("Enter amount to deposit: "))
                self.balance += amount
                print("Deposited successfully.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        else:
            print("Invalid PIN number.")

    def withdraw(self):
        """Withdraw money after verifying PIN and checking balance."""
        pin = input("Enter PIN number: ")
        if pin == self.pin:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= self.balance:
                    self.balance -= amount
                    print("Withdraw successful.")
                else:
                    print("Insufficient funds.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        else:
            print("Invalid PIN number.")

    def check_funds(self):
        """Display current balance after verifying PIN."""
        pin = input("Enter PIN number: ")
        if pin == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Invalid PIN number.")


# Usage
print(Atm.__doc__)   # Shows class documentation
sbi = Atm()
sbi.menu()