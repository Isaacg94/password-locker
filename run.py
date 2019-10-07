#!/usr/bin/env python3.6
from passwords import User, Credentials

def create_user (fname, lname, password):
    """
    Function to create a new user.
    """
    new_user = User(fname, lname, password)
    return new_user

def save_user(user):
    """
    Function to create new user.
    """
    User.save_user(user)

def user_exists(first_name, password):
    """
    Function to verify user exists.
    """
    checking_user = User.check_user(first_name, password)
    return checking_user

def create_credential(site, user_name, password):
    """
    Function that creates new credentials.
    """
    new_credential = Credentials(site, user_name, password)
    return new_credential

def save_credentials(credential):
    """
    Function to save new credentials.
    """
    Credentials.save_credential(credential)

def display_credentials(user_name):
    """
    Function to display saved credentials.
    """
    return Credentials.display_credential(user_name)



def main():
    print('\n')
    print("Welcome To Your Keychain.")
    while True:
        print('')
        print("Use these codes to navigate: \n sa - Create account \n si - Sign in \n ex - Exit")
        print("Enter a choice")
        short_code = input()

        if short_code == 'sa':
            print("Create new account:")
            print("Enter your first name:")
            first_name = input()
            print("Enter your second name:")
            last_name = input()
            print("Enter your password:")
            password = input()
            save_user(create_user(first_name, last_name, password))
            print(f"New account created for {first_name} {last_name} with the following password: {password}")

        elif short_code == 'si':
            print("Enter account details to sign-in")
            print("Enter your first name")
            user_name = input()
            print("Enter your password")
            password = str(input())
            user_exists = user_exists(user_name, password)
            if user_exists == user_name:
                print(f"Welcome {user_name}. Decide how you would like to proceed.")
                while True:
                    print("Use: \n sc - Create Credential \n sd - Display Credential \n sp - Copy \n ex - Exit")
                    print("Enter a choice")
                    short_code = input()
                    if short_code = 'sc':
                        print("Enter Credential Details:")
                        print("Enter site name")
                        site = input()
                        print("Enter your username")
                        user_name = input()
                        print("Enter password")
                        password = input()

                        save_credentials(create_credential(site, user_name, password))

                        print(f"Credential created for {site} - Account name: {user_name} - Password: {password}")

                    elif short_code == 'sd':
                        if display_credentials(user_name):
                            print("Here are your credentials")

                            for credential in display_credentials(user_name):
                                print(f"Site: {credential.site} \n Account name: {credential.user_name} \n Password: {credential.password}")
                            else:
                                print("You do not have any saved credentials")

                    elif short_code == 'ex':
                        break

                    else:
                        print("Invalid input. Try again.")


            else:
                print("Account not found")

        elif short_code == 'ex':
            break

        else:
            print("Invalid input. Try again")

if __name__ == '__main__':
    main()