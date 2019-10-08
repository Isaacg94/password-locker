import pyperclip


class User:
    """
    Class that stores new instances of users.
    """

    users_list = []

    def __init__(self, first_name, last_name, password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        """
        method that saves user new user objects to empty users list.
        """
        User.users_list.append(self)

    @classmethod
    def check_user(cls, first_name, password):
        """
        Method that checks if the names and password match the ones in users list.
        """
        current_user = ""
        for user in cls.users_list:
            if(user.first_name == first_name and user.password == password):
                return True
        return False


class Credentials:
    """
    Class that stores new instances of users credentials.
    """
    credentials_list = []
    # users_credentials_list = []

    def __init__(self, site, user_name, password):

        self.site = site
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        """
        Method that saves credential objects in the credentials list.
        """
        Credentials.credentials_list.append(self)

    @classmethod
    def display_credential(cls):
        """
        Class method that displays saved credentials.
        """
        # user_credentials_list = []
        # for credential in cls.credentials_list:
        #     if credential.site == site:
        #         user_credentials_list.append(credential)
        return cls.credentials_list

    @classmethod
    def find_by_site(cls, site):
        """
        Class method that allows credentials to be found through site name.
        """
        for credential in cls.credentials_list:
            if credential.site == site:
                return credential

    @classmethod
    def copy_credential(cls, site):
        """
        Method that allows credentials to be copied.
        """
        find_credential = Credentials.find_by_site(site)
        return pyperclip.copy(find_credential.password)
