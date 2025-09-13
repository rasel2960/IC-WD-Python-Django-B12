# This is a simple bank account management system.
# Developed by Rasel Ahmed.
# E-mail: ah.moon90@gmail.com

import json
from datetime import datetime

class BankSystem:
    def __init__(self):
        pass

    def handle_existing_user(self):

        # Load existing customer data
        try:
            with open('customers.json', 'r') as file:
                all_customers = json.load(file)
        except FileNotFoundError:
            print("No existing accounts found. Please create a new account first.")
            return

        # Collect User Account Number
        while True:
            user_account = input("Please enter your account number\n (or type 'exit' to quit):\n> ").strip()
            if user_account == 'exit':
                print("Thank you for using Bank Account Management System")
                return

            # user_account Validation
            if not user_account.isdigit() or len(user_account) != 10:
                print("Invalid account number. It should be a 10-digit number.")
                continue

            # Check if account exists
            if user_account not in all_customers:
                print("Account number not found. Please try again or create a new account.")
                continue
            break

        # Collect User Account Password
        while True:

            user_password = input("Please enter your account password\n (or type 'exit' to quit):\n> ").strip()
            if user_password == 'exit':
                print("Thank you for using Bank Account Management System")
                return
            # Check if password matches
            if user_password != all_customers[user_account]['ac_password']:
                print("Incorrect password. Please try again.")
                continue
            break

        # Print successful login  message
        print(f"Welcome back, {all_customers[user_account]['ac_title']}. You have successfully logged in to your account.")

        # Show account menu
        self.show_account_menu(user_account, all_customers)

    def handle_new_user(self):
        # Create a new Bank Account
        print(f"\nWelcome to the Bank Account Management System")
        print("Let's create your new bank account.")

        # Step 1 : Collect User Account Number

        print(f"\nYour account number will start with '0112'")
        while True:
            user_digits = input(
                "Please enter the last 6 digits of your desired account number \n(or type 'exit' to quit):\n > ").strip()

            if user_digits == 'exit':
                print("Thank you for using Bank Account Management System")
                return

            if not user_digits.isdigit() or len(user_digits) != 6:
                print("Invalid input. It should be a 6-digit number.")
                continue
            else:
                ac_number = '0112' + user_digits
                # Check if ac_number already exists
                try:
                    with open('customers.json', 'r') as file:
                        all_customers = json.load(file)
                    if ac_number in all_customers:
                        print("This account number already exists. Please choose a different one.")
                        continue
                except FileNotFoundError:
                    # If file does not exist, we can proceed as no accounts exist yet
                    pass

                print(f"Your account number {ac_number} has been created successfully!")
            break

        # Step 2 : Collect User Account Title
        while True:
            ac_title = input("Please enter your Account Title:\n > ").strip().title()
            # Check ac_title is not empty
            if len(ac_title) <= 0:
                print("Account Title can't be empty.")
                continue
            break


        # Step 3 : Collect User Account Password
        while True:
            ac_password = input("\nPlease enter password for your account\nor type 'exit' to quit:\n"
                                "Password length should be 4 - 8 character\n > ").strip()
            if ac_password == 'exit':
                print("Thank you for using Bank Account Management System")
                return

            if len(ac_password) < 4 or len(ac_password) > 8:
                print("Password should be at least 4 or max 8 characters long.")
                continue
            else:
                print(f"Your account password has been set successfully!")

            break

        # Step 4 : Store ac opening time with initial balance
        ac_open_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_balance = 0

        # Create a dictionary to store user account details
        ac_info = {
            "ac_title": ac_title,
            "ac_number": ac_number,
            "ac_password" : ac_password,
            "ac_open_date": ac_open_date,
            "current_balance": current_balance,
        }

        # Display account creation success message
        print("\n========= Account created successfully! =========")
        print(f"\tHere are your account details:")
        print(f"\t- Account Title: {ac_title}")
        print(f"\t- Account Number: {ac_number}")
        print(f"\t- Account Opening Date: {ac_open_date}")
        print(f"\t- Current Balance: Tk. {current_balance:.2f}")
        print("Please keep your account number and password safe.")
        print("====================================================")

        # Save account info to a JSON file
        try:
            # Load existing customer data
            with open('customers.json', 'r') as file:
                all_customers = json.load(file)
        except FileNotFoundError:
            # In case file does not exist, start with an empty dict
            all_customers = {}

        # Add new customer (using ac_number as key)
        all_customers[ac_number] = ac_info

        # Save updated customer data back to the file
        with open('customers.json', 'w') as file:
            json.dump(all_customers, file, indent=4)
        print("Your account information has been saved successfully!")


    # Check Balance Method
    def check_balance(self, user_account, all_customers):
        customer_account = all_customers[user_account]['ac_number']
        customer_name = all_customers[user_account]['ac_title']
        current_balance = all_customers[user_account]['current_balance']
        balance_str = f"Tk. {current_balance:.2f}"

        # Calculate column widths for formatting
        header1, header2, header3 = "Account Number", "Account Title", "Current Balance"
        col1_width  = max(len(header1), len(customer_account))
        col2_width  = max(len(header2), len(customer_name))
        col3_width  = max(len(header3), len(f"Tk. {current_balance:.2f}"))

        # Create formatted rows using Python string formatting
        header_row = "{:<{}} | {:<{}} | {:>{}}".format(header1, col1_width, header2, col2_width, header3, col3_width)
        separator = f"{'-' * col1_width}-+-{'-' * col2_width}-+-{'-' * col3_width}"
        data_row = "{:<{}} | {:<{}} | {:>{}}".format(customer_account, col1_width, customer_name, col2_width, balance_str, col3_width)


        while True:
            # Display the table
            print(f"\n{header_row}")
            print(separator)
            print(data_row)
            break

        # Wait for user to press Enter to return to menu
        user_choice = input("\nPress Enter to go to Account Menu\n> ")

    # Implementation of Deposit Money Method
    def deposit_money(self, user_account, all_customers):

        try:
            amount = float(input("Please Enter Deposit Amount: Tk. "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        else:
            current_balance = all_customers[user_account]['current_balance'] + amount
            all_customers[user_account]['current_balance'] = current_balance

        trxn_description = input("Enter transaction description : ").strip().capitalize()
        if not trxn_description:
            trxn_description = "Cash Deposit"

        trxn_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Create Transaction Record
        transaction = {
            "date": trxn_date,
            "description": trxn_description,
            "debit": None,
            "credit": amount,
            "closing_balance": current_balance,
        }

        # Store Transaction History
        if 'transaction_history' not in all_customers[user_account]:
            all_customers[user_account]['transaction_history'] = []
        # Append the new transaction to the user's transaction history
        all_customers[user_account]['transaction_history'].append(transaction)

        # Save Transaction History to JSON file
        with open('customers.json', 'w') as file:
            json.dump(all_customers, file, indent=4)

        print(f"\nSuccessfully deposited Tk. {amount:.2f}.\nYour New balance is Tk. {all_customers[user_account]['current_balance']:.2f}")

        user_choice = input("\nPress Enter to go to Account Menu\n> ")

    # Implementation of Withdraw Money Method
    def withdraw_money(self, user_account, all_customers):
        current_balance = all_customers[user_account]['current_balance']
        try:
            amount = float(input("Please Enter Withdrawal Amount: Tk. "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return

        # 1. Zero/Negative Amount Check
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        # 2. Sufficient Balance Check
        if amount > current_balance:
            print("You don't have sufficient balance for this withdrawal.")
            print(f"Your current balance is Tk. {current_balance:.2f}")
            return
        # 3. Minimum Balance Check (Assuming minimum balance is Tk. 500)
        if current_balance - amount < 500:
            print("Minimum balance of Tk. 500 must be maintained after withdrawal.")
            print(f"Maximum withdrawable amount is Tk. {current_balance - 500:.2f}")
            return

        else:
            current_balance = all_customers[user_account]['current_balance'] - amount
            all_customers[user_account]['current_balance'] = current_balance

        trxn_description = input("Enter transaction description : ").strip().capitalize()
        if not trxn_description:
            trxn_description = "Cash Withdrawal"

        trxn_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Create Transaction Record
        transaction = {
            "date": trxn_date,
            "description": trxn_description,
            "debit": amount,
            "credit": None,
            "closing_balance": current_balance,
        }

        # Store Transaction History
        if 'transaction_history' not in all_customers[user_account]:
            all_customers[user_account]['transaction_history'] = []
        # Append the new transaction to the user's transaction history
        all_customers[user_account]['transaction_history'].append(transaction)

        # Save Transaction History to JSON file
        with open('customers.json', 'w') as file:
            json.dump(all_customers, file, indent=4)

        print(f"\nYour account has been debited Tk. {amount:.2f}.\nYour New balance is Tk. {all_customers[user_account]['current_balance']:.2f}")
        user_choice = input("\nPress Enter to go to Account Menu\n> ")


    # View Account Statement
    def view_account_statement(self, user_account, all_customers):
        # Check if Transactions exists in History
        if 'transaction_history' not in all_customers[user_account]:
            print("No Transaction Found!")
            input("\nPress Enter to return to Account Menu\n> ")
            return

        transactions = all_customers[user_account]['transaction_history']

        # Print Customer Info as Header
        print("=" * 77)
        print(f"{'Account Number':<16} : {user_account}")
        print(f"{'Account Title':<16} : {all_customers[user_account]['ac_title']}")
        print("=" * 77)

        # Printing Statement Header Row
        print(f"{'Trxn Date':<10} | {'Description':<20} | {'Debit':>10} | {'Credit':>10} | {'Closing Balance':>15}")
        print("=" * 77) # Line Separator

        # Printing Each Transactions in Each Row
        for transaction in transactions:
            date = transaction['date'][:10]
            description = transaction['description']
            debit = f"{transaction['debit']:.2f}" if transaction['debit'] else ""
            credit = f"{transaction['credit']:.2f}" if transaction['credit'] else ""
            closing_balance = f"{transaction['closing_balance']:.2f}"

            print(f"{date:<10} | {description:<20} | {debit:>10} | {credit:>10} | {closing_balance:>15}")


        # Print Total Transaction Summary
        total_debit = sum(t['debit'] for t in transactions if t['debit'])
        total_credit = sum(t['credit'] for t in transactions if t['credit'])

        print("=" * 77)  # Line Separator
        print(f"{'':<10} | {'Total':<20} | {total_debit:>10.2f} | {total_credit:>10.2f} | {'':>15}")
        print("=" * 77)  # Line Separator

        input("\nPress Enter to return to Account Menu\n> ")



    def show_account_menu(self, user_account, all_customers):
        customer_name = all_customers[user_account]['ac_title']
        account_number = all_customers[user_account]['ac_number']

        while True:
            # Display Personalized Menu Header
            print(f"\n===================================================")
            print(f"Welcome back, {customer_name}!")
            print(f"Account Number: {account_number}")
            print(f"===================================================")

            # Display Menu Options
            print(f"\n======= General Banking Menu ========")
            print(f"\t1. Check Balance")
            print(f"\t2. Deposit Money")
            print(f"\t3. Withdraw Money")
            print(f"\t4. View Transaction History")
            print(f"\t5. Exit")
            print(f"=====================================")
            print(f"Choose an option (1-5): ")
            user_choice = input("> ").strip()
            if user_choice == '1':
                self.check_balance(user_account, all_customers)
            elif user_choice == '2':
                self.deposit_money(user_account, all_customers)
            elif user_choice == '3':
                self.withdraw_money(user_account, all_customers)
            elif user_choice == '4':
                self.view_account_statement(user_account, all_customers)
            elif user_choice == '5':
                print("Exiting the Program...")
                break
            else:
                print("Invalid choice. Please select a valid option (1-5).")





    def welcome_screen(self):
        print("Welcome to the Bank Account Management System")

        while True:
            user_response = input("\nDo you have an account with us? (Y/N)\nor type 'exit' to quit:\n> ").strip().lower()
            if user_response == 'exit':
                print("Thank you for using Bank Account Management System.")
                break
            elif user_response == "y":
                self.handle_existing_user()
                break
            elif user_response == "n":
                self.handle_new_user()
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N' or 'exit'.")


if __name__ == "__main__":
    bank = BankSystem()
    bank.welcome_screen()