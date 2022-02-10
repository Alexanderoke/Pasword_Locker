from user import User, Credentials
import pyperclip


def register_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function storing a new user
    '''
    user.save_user()

def display_user():
    """
    Function to display registered user
    """
    return User.display_user()

def login_user(username,password):
    """
    function that user is registered and can be logrd in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def Register_user_details(account,userName,password):
    """
    Function to register new user details for an account
    """
    new_details = Credentials(account,userName,password)
    return new_details
def save_credentials(credentials):
    """
    Function to store Credentials to the credentials list
    """
    credentials. store_details()
def display_accounts_details():
    """
    Function to bring all stored credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function to finds acccount details by name and returns the detaails that belong to the same account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    function copies password using pyperclip package
    We import the package then declare a function that copies the passwords.
    """
    return Credentials.copy_password(account)


def pass_locker():
    print("Welcome to the Password Manager..\n write one of the following to continue.\n R ---  Register New Account  \n L ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "r":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print("OP - To type your own pasword:\n G - System generate Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'op':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'g':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(register_user(username,password))
        print("*#*#*#*#*#*#*#*#*#*#*#*#*##*##*#*##*#*#*#*#*#*#*#*#*#*#*#*##*#*#*#*#*#*#*#*#*##*#*##*#*#*#*#*#*#*#*#*#*#*#")
        print(f"{username}, Your account has been created succesfully! Your password is: {password}")
        print("*#*#*#*#*#*#*###*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    elif short_code == "l":
        print("*#*#*#*#*#*#*#*#*#*#*#*#*##*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*##*#*#*##*#*#*#*#*##*#*#*#**#")
        print("Enter your User name and your Password to log in:")
        print('*#*#*#*#*#*#*#*#*#*###*#*#*#*#*#*#*#*#*###*#*#*#*#*#*#*##*#*##*###*#*#*#*#*#*#*#*##*#*#*#*#*#*#*#*#*#*#**#*#*#*#*')
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To The PassWord Manager")  
            print('\n')
    while True:
        print("Use these short codes:\n R - Create a new credential \n S - Show Credentials \n F - Find a credential \n G - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "r":
            print("Create New Credential")
            print(".#*#*#*#*#*#*#*#*#*#*#*#*##*#*#*#*#*#*#*#*#*#")
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" OP - To type your own pasword if you already have an account:\n G - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'op':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'g':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(Register_user_details(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "d":
            if display_accounts_details():
                print("Here are your acoounts: ")
                 
                print('*#*#*#*#*#**#*#*#*#*#*#*#**#*#*#*##*#*#*#*#*#*#*#*#*##*#*#*#**#*#*#*#*#*##*#*#')
                print('********************************************************************************')
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('******************************************************************************')
                print('*' * 30)
            else:
                print("No credentials stored..")
        elif short_code == "f":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('****************************************************************************************')
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('*****************************************************************************************')
            else:
                print("That does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("********************************************************************************************")
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'g':

            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords manager..")
            break
        else:
            print("Wrong entry... Check your entry  and try again")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    pass_locker()