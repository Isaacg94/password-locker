#!/usr/bin/env python3.6
import pyperclip
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

def delete_credentials(credential):
    """
    Function to delete a credential.
    """
    Credentials.delete_credential(credential)

def display_credentials():
    """
    Function to display saved credentials.
    """
    return Credentials.display_credential()

def find_by_site(site):
    """
    Function to find credential by site.
    """
    return Credentials.find_by_site(site)
def copy_password(site):
    """
    Function to copy password.
    """
    return Credentials.copy_password(site)


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
            first_name = input()
            print("Enter your password")
            password = str(input())
            # user_exists = user_exists(first_name, password)
            if user_exists(first_name, password):
                print(f"Welcome {first_name}. Decide how you would like to proceed.")
                while True:
                    print("Use: \n sc - Create Credential \n sd - Display Credential \n dl - Delete Credentials \n ex - Exit")
                    print("Enter a choice")
                    short_code = input()
                    if short_code == 'sc':
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
                        if len(display_credentials()) >= 1:
                            print("Here are your credentials")

                            for credential in display_credentials():
                                print(f"Site: {credential.site} \n Account name: {credential.user_name} \n Password: {credential.password}")
                        else:
                            print("You do not have any saved credentials")

                    # elif short_code == 'sp':
                    #     print("Enter the name of the credential you would like to copy")
                    #     cpy_credit = input()
                    #     srch_credit = find_by_site(cpy_credit)
                    #     copy_password(srch_credit.password) 
                    #     print("Credential has been copied successfully")

                    elif short_code == 'dl':
                        if len(display_credentials()) >= 1:
                            print("Enter the name of the credential you would like to delete")
                            del_credit = input()
                            found_cred = find_by_site(del_credit)
                            delete_credentials(found_cred)
                            print("Credential has been deleted successfully")
                        else:
                            print("No Credential to delete")

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