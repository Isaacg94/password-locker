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


class Credentials:
    """
    Class that stores new instances of users credentials.
    """
    credentials_list = []

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
    def display_credential(cls, user_name):
        """
        Class method that displays saved credentials.
        """
        users_credentials_lists = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                users_credentials_lists.append(credential)
        return users_credentials_lists

    @classmethod
    def find_by_site(cls, site):
        """
        Class method that allows credentials to be found through site name.
        """
        for credential in cls.credentials_list:
            if credential.site == site:
                return credential