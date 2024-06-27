# Global dictionary to store account information
accounts = {}
next_account_number = 1

# New account info is stored here
def create_account(name, initial_balance):
    global next_account_number
    account_number = next_account_number
    accounts[account_number] = {
        "name": name,
        "balance": initial_balance
    }
    next_account_number += 1
    return account_number

# Deposit function
def deposit(account_number, amount):
    if account_number in accounts:
        accounts[account_number]["balance"] += amount
        return accounts[account_number]["balance"]
    else:
        return "Account not found."

# Withdraw function
def withdraw(account_number, amount):
    if account_number in accounts:
        if accounts[account_number]["balance"] >= amount:
            accounts[account_number]["balance"] -= amount
            return accounts[account_number]["balance"]
        else:
            return "Insufficient funds."
    else:
        return "Account not found."

# Balance function
def check_balance(account_number):
    if account_number in accounts:
        return accounts[account_number]["balance"]
    else:
        return "Account not found."

# Main function to take innputs from the user
def main():
    while True:
        print("\n1. Create account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            initial_balance = float(input("Enter the amount of balance you want to store : "))
            account_number = create_account(name, initial_balance)
            print(f"Your account is created with number: {account_number}")

        elif choice == '2':
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter the amount you want to deposit: "))
            new_balance = deposit(account_number, amount)
            print(f"Your new balance is : {new_balance}")

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount you want to withdraw: "))
            new_balance = withdraw(account_number, amount)
            print(f"Your new balance is : {new_balance}")

        elif choice == '4':
            account_number = int(input("Enter account number: "))
            balance = check_balance(account_number)
            print(f"Your current balance is : {balance}")

        elif choice == '5':
            break

if __name__ == "__main__":
    main()
