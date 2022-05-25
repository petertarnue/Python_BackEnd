# The CRUD method of database creation

import os
import validation

user_db_path = 'data/user_records/'


def create_user_record(account_number, first_name ,last_name , email, password):   # create record

    user_data = first_name + ',' + last_name + "," + email + "," + password + "," + str(0)
    
    if does_account_number_exist(account_number):
        return False
   
    if does_email_exist(email):
        print("User already exist")
        return False

    completion_state = False
    
    try:
        # name of the file would be account_number.txt
        file = open(user_db_path + str(account_number) + ".txt", 'x')
        
    except:
        does_fil_contain_data = read_user_record(user_db_path + str(account_number) + ".txt",)
        
        # check user content before deleting file
        if not does_fil_contain_data:
            # delete the already created file and print out error, then return false
            delete_user_record(account_number)
        
    else:
        # add th user details to the file 
        file.write(str(user_data))
        # return true 
        completion_state = True
    
    finally:
        file.close()
        return completion_state


def read_user_record(user_account_number):   # read record
    # find user with account number
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:
        
        if is_valid_account_number:
            
            file = open(user_db_path + str(user_account_number) + ".txt", 'r')
            
        else:
            
            file = open(user_db_path + user_account_number, 'r')
            
    except FileNotFoundError:
        
        print("User was not found")
        
    except FileExistsError:
        
        print("User doesn't exist")
        
    except TypeError:
        
        print("Invalid account format")
        
    else:
        # read user detials
        read_file = file.readline()
        
        return read_file
    
    return False 


def update_user_record(account_number):  # update record
    print('update user account record')
    # find user with account number
    # fitch the content of the file 
    # update the content of the file
    # save the file   
    # return True


def delete_user_record(account_number):  # delete record
    # find user with account number
    is_delete_successful = False

    if os.path.exists(user_db_path + str(account_number) + '.txt'):
        try:
            # delete user record (file)
            # check content of file before deleting 
            os.remove(user_db_path + str(account_number) + '.txt')
            is_delete_successful = True

        except FileNotFoundError:
            print("User was not found")
        finally:
            # return True
            return is_delete_successful


def does_email_exist(email):
    # list the directory of all the user account detail

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read_user_record(user),',')
        if email in user_list:
            return True 
        return False


def does_account_number_exist(account_number):
    # locate the list of users in database folder
    all_users = os.listdir(user_db_path) 
    
    for users in all_users:
        if users == str(account_number) + '.txt': 
            return True 
        return False 

    
def authenticated_user(account_number, password):
    
    if does_account_number_exist(account_number):
        
        user = str.split(read_user_record(account_number), ',')
        
        if password == user[3]:
            
            return user
    
    return False 

        
# print(authenticated_user(1727035946, 'password'))

# print(read_user_record(2070823818))

# print(does_email_exist('kelvintarnue@gmail.com'))

# print(does_account_number_exist(5983244318)