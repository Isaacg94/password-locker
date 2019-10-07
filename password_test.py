import unittest
import pyperclip
from passwords import User, Credentials


class TestUser(unittest.TestCase):
    """
    Test class that tests the User class.
    """

    def setUp(self):
        """
        Method that will run before each test.
        """
        self.new_user = User("Isaac", "Gichuru", "123456")

    def test__init__(self):
        """
        Method to d=test if object is instanciated properly.
        """
        self.assertEqual(self.new_user.first_name, "Isaac")
        self.assertEqual(self.new_user.last_name, "Gichuru")
        self.assertEqual(self.new_user.password, "123456")

    def tearDown(self):
        """
        A method that clears the users object after test.
        """
        User.users_list = []

    def test_save_user(self):
        """
        Test case to check if new user object can be saved to empty user list.
        """
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)

    def test_check_user(self):
        """
        Method to test login function works correcty.
        """
        self.new_user = User("isaac", "gichuru", "123456")
        self.new_user.save_user()
        user1 = User("Penina", "Wambui", "654321")
        user1.save_user()

        for user in User.users_list:
            if user.first_name == user1.first_name and user.password == user1.password:
                current_user = user.first_name,
        return current_user

        self.assertEqual(current_user, User.check_user(user1.password, user1.first_name))


class TestCredentials(unittest.TestCase):
    """
    Test class that tests the credentials class.
    """

    def setUp(self):
        """
        Method that will run before each test.
        """
        self.new_credential = Credentials("Instagram", "isaacgish", "123456")

    def test__init__(self):
        """
        Test case to check if credential instances are created correctly.
        """
        self.assertEqual(self.new_credential.site, "Instagram")
        self.assertEqual(self.new_credential.user_name, "isaacgish")
        self.assertEqual(self.new_credential.password, "123456")

    def test_save_credential(self):
        """
        Test if credentials can be saved to the empty credential list.
        """
        self.new_credential.save_credential()
        instagram = Credentials("instagram", "isaacgish", "123456")
        instagram.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def tearDown(self):
        """
        A method that clears the credentials object after test.
        """
        Credentials.credentials_list = []

    def test_display_credential(self):
        """
        Test to check if credentials can be displayed.
        """
        self.new_credential.save_credential()
        instagram = Credentials("instagram", "isaacgish", "123456")
        instagram.save_credential()
        self.assertEqual(
            len(Credentials.display_credential(instagram.user_name)), 2)

    def test_find_by_site(self):
        """
        Method to test if credentials can be searched by site correctly.
        """
        self.new_credential.save_credential()
        instagram = Credentials("instagram", "isaacgish", "123456")
        instagram.save_credential()
        credential_exists = Credentials.find_by_site("instagram")
        self.assertEqual(credential_exists, instagram)

    # def test_copy_credential(self):
    #     """
    #     Method to test if the copy credential function works correctly.
    #     """
    #     self.new_credential.save_credential()
    #     instagram = Credentials("instagram", "isaacgish", "123456")
    #     instagram.save_credential()
    #     find_credential = None
    #     for credential in Credentials.users_credentials_lists:
    #         find_credential = Credentials.find_by_site(credential.site)
    #         return pyperclip.copy(find_credential.password)
    #     Credentials.copy_credential(self.new_credential.password)
    #     self.assertEqual("123456", pyperclip.paste())
    #     print(pyperclip.paste())


if __name__ == "__main__":
    unittest.main()
