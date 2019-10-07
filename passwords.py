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


    def __init__(self, site, user_name, password):

        self.site = site
        self.user_name = user_name
        self.password = password
