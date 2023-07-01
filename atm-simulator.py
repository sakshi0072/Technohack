class ATM:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance"

# Create an instance of the ATM
atm = ATM("123456789", "1234", 1000)

# Prompt the user for account number and PIN
account_number = input("Enter your account number: ")
pin = input("Enter your PIN: ")

# Validate the account number and PIN
if account_number == atm.account_number and pin == atm.pin:
    while True:
        # Display the menu
        print("\nATM Simulator")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            # Check Balance
            balance = atm.check_balance()
            print(f"Your current balance is: ${balance}")
        
        elif choice == "2":
            # Deposit
            amount = float(input("Enter the amount to deposit: $"))
            new_balance = atm.deposit(amount)
            print(f"Deposit successful. Your new balance is: ${new_balance}")
        
        elif choice == "3":
            # Withdraw
            amount = float(input("Enter the amount to withdraw: $"))
            new_balance = atm.withdraw(amount)
            
            if isinstance(new_balance, str):
                print(new_balance)
            else:
                print(f"Withdrawal successful. Your new balance is: ${new_balance}")
        
        elif choice == "4":
            # Exit
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

else:
    print("Invalid account number or PIN. Access denied.")
