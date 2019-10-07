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