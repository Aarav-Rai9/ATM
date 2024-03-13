import datetime

class Account:
    def __init__(self, name, account_number, pin):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append((datetime.datetime.now(), 'Deposit', amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append((datetime.datetime.now(), 'Withdrawal', amount))
        else:
            print("Insufficient funds")

    def check_balance(self):
        return f"Your current balance is: ${self.balance}"

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(f"{transaction[0]} - {transaction[1]}: ${transaction[2]}")


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number, pin):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(name, account_number, pin)
            print("Account created successfully!")
        else:
            print("Account number already exists. Please choose another.")

    def select_account(self, account_number, pin):
        if account_number in self.accounts:
            if self.accounts[account_number].pin == pin:
                return self.accounts[account_number]
            else:
                print("Incorrect PIN. Access denied.")
        else:
            print("Account does not exist.")

    def deposit(self, account, amount):
        account.deposit(amount)
        print(f"Successfully deposited ${amount}")

    def withdraw(self, account, amount):
        account.withdraw(amount)

    def check_balance(self, account):
        print(account.check_balance())

    def show_transaction_history(self, account):
        account.show_transaction_history()


def atm_interface():
    atm = ATM()

    while True:
        print("\nOptions:")
        print("1. Create New Account")
        print("2. Access Existing Account")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name = input("Enter your name: ")
            account_number = input("Enter desired account number: ")
            pin = input("Enter PIN for the account: ")
            atm.create_account(name, account_number, pin)
        elif choice == '2':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            selected_account = atm.select_account(account_number, pin)
            if selected_account:
                print("Account selected successfully!")
                while True:
                    print("\nAccount Options:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Go Back")

                    account_choice = input("Enter your choice (1-5): ")

                    if account_choice == '1':
                        amount = float(input("Enter amount to deposit: $"))
                        atm.deposit(selected_account, amount)
                    elif account_choice == '2':
                        amount = float(input("Enter amount to withdraw: $"))
                        atm.withdraw(selected_account, amount)
                    elif account_choice == '3':
                        atm.check_balance(selected_account)
                    elif account_choice == '4':
                        atm.show_transaction_history(selected_account)
                    elif account_choice == '5':
                        print("Returning to main menu.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_interface()
