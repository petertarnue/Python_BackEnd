import random
import validation
import database
from getpass import getpass


# login
# first name, last name and email address
# (email and passWord

# bank Operations

# initializing the system


def init():
    print("Welcome to the United Bank of Liberia Limited")
    have_account = int(input("Do you have an account with us? 1 (yes), 2 (no) \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have enter an Invalid response")
        init()


def login():
    print("***************** Login*************")
    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        # password = input("Enter a valid password for your account \n")

        password = input("Enter a valid password for your account \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operations(user)

        print("Invalid account or password")
        login()

    else:
        print('Account number Invalid: Check that you have upto 10 digit only integers')
        init()


def register():
    print("****** Register *********")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("what is your email address? \n")

    password = input("Create a unique password for your account \n")

    account_number = generate_user_account()

    is_user_created = database.create_user_record(account_number, first_name, last_name, email, password)

    if is_user_created:
        print("Your account has been created")
        print("==== ==== ==== ===")
        print("Your account number is %s " % account_number)
        print("Make sure you keep it safe")
        print("** === === === === ** ")

        login()
    else:
        print('Something went wroing')
        register()


def bank_operations(user):
    print("Welcome %s " % user[0], user[1])

    selected_option = int(input('What would like to do? (1) Deposit (2) Withdrawal (3) Login (4) exit \n'))
    if selected_option == 1:
        deposit_operation()
    elif selected_option == 2:
        withdrawal_operation()
    elif selected_option == 3:
        login()
    elif selected_option == 4:
        exit()
    else:
        print("invalid option selected ")
        bank_operations(user)
    print("Do you want to do another operation? 1 (yes), 0 (no)")

    new_transaction = int(input('Enter 1 to do another transaction and 2 to exit transaction \n'))
    if new_transaction == 1:
        bank_operations(user)
    elif new_transaction == 0:
        exit()


def withdrawal_operation(account_number):
    # get current balance
    try:
        user_balance = get_user_balance(account_number)

        # get amount to withdrawal
        withdrawal_amount = int(input('Enter the amount you want to withdral \n'))

        # check if current balance > withdrawal balance
        if user_balance > withdrawal_amount:

            if user_balance > 20:
                user_balance - withdrawal_amount
            return user_balance
            # deduct withdral balance from current balance
        # display current balance 
    except:
        exit()
    print("We were not able to get your your balance due to internet failure ")


def deposit_operation():
    # get the user balance
    user_balance = get_user_balance()
    # get the amount to deposit
    deposit = int(input("Enter the amount that you want to deposit"))
    # Add deposit to user balance
    user_balance = deposit + user_balance
    return user_balance

    print("deposit operations")


def generate_user_account():
    account_number = random.randrange(1111111111, 9999999999)
    return account_number


def get_user_balance(user_details):
    return user_details[4]


# Actual Banking System

init()
