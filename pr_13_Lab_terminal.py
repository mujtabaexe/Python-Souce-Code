'''
Name:Muhammad Hamza Habib
Registration number:SP24_BAI-034
Exam: Lab Terminal
Date: 1-june-2024
'''

accounts = {}  # We are taking dictionary for storing informations about accoount
account_counter = 1

#creating function for account creation with the name create_account
def create_account(name, initial_balance):
    global account_counter
    account_number = account_counter
    accounts[account_number] = {
        'name': name,
        'balance': initial_balance
    }
    account_counter += 1
    return account_number

#creating function for depositing money with the name 'deposit'
def deposit(account_number, amount):
    if account_number in accounts:
        accounts[account_number]['balance'] += amount
        return accounts[account_number]['balance']
    else:
        return "Account not found."

#creating function for withdrawing money with the name 'withdraw'
def withdraw(account_number, amount):
    if account_number in accounts:
        if accounts[account_number]['balance'] >= amount:
            accounts[account_number]['balance'] -= amount
            return accounts[account_number]['balance']
        else:
            return "Insufficient funds."
    else:
        return "Account not found."

#creating function for checking balence of your account with the name 'check_balence'
def check_balance(account_number):
    if account_number in accounts:
        return accounts[account_number]['balance']
    else:
        return "Account not found."

def main():
    while True:
        print("\nBanking System Menu:")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter the account holder's name: ")
            initial_balance = float(input("Enter the initial balance: "))
            account_number = create_account(name, initial_balance)
            print(f"Account created successfully. Your account number is {account_number}.")

        elif choice == '2':
            account_number = int(input("Enter the account number: "))
            amount = float(input("Enter the amount to deposit: "))
            updated_balance = deposit(account_number, amount)
            if isinstance(updated_balance, str):
                print(updated_balance)
            else:
                print(f"Deposit successful. Updated balance: {updated_balance}")

        elif choice == '3':
            account_number = int(input("Enter the account number: "))
            amount = float(input("Enter the amount to withdraw: "))
            updated_balance = withdraw(account_number, amount)
            if isinstance(updated_balance, str):
                print(updated_balance)
            else:
                print(f"Withdrawal successful. Updated balance: {updated_balance}")

        elif choice == '4':
            account_number = int(input("Enter the account number: "))
            balance = check_balance(account_number)
            if isinstance(balance, str):
                print(balance)
            else:
                print(f"Current balance: {balance}")

        elif choice == '5':
            print("Thank you for using the banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
