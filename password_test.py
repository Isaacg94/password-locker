import unittest
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

    def test_save_user(self):
        """
        Test case to check if new user object can be saved to empty user list.
        """
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)


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

    def test_display_credential(self):
        """
        Test to check if credentials can be displayed.
        """
        self.new_credential.save_credential()
        instagram = Credentials("instagram", "isaacgish", "123456")
        instagram.save_credential()
        self.assertEqual(len(Credentials.display_credential(instagram.user_name)), 2)


if __name__ == "__main__":
    unittest.main()
