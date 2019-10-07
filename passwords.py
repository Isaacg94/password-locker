class User:
    """
    Class that stores new instances of users.
    """



def __init__(self, first_name, last_name, password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password


class Credentials:
    """
    Class that stores new instances of users credentials.
    """


credentials_list = []


def __init__(self, site, user_name, password):

        self.site = site
        self.user_name = user_name
        self.password = password


new_credential = Credentials("instagram", "isaacg94", "12345678")

print(new_credential.site,new_credential.user_name,new_credential.password)
