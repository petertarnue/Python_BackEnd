
def account_number_validation(account_number):
    # chech if account number is empty
    # if account number is 10 digits
    # if account number is an integer 

    if account_number:
        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

        except ValueError:

            return False

    elif len(str(account_number)) < 10:

        return False

    else:

        return False

