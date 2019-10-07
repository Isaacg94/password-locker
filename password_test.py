import unittest
from passwords import User


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
        self.assertEqual(len(User.users_list),1)


class TestCredentials(unittest.TestCase):
    """
    Test class that tests the credentials class.
    """
    def setUp(self):
        """
        Method that will run before each test.
        """
        self.new_credential = Credentials("Instagram", "Isaacgish", "123456")

    def test__init__(self):
        """
        Test case to check if credential instances are created correctly.
        """
        self.assertEqual(self.new_credential.site, "Instagram")
        self.assertEqual(self.new_credential.user_name, "isaacgish")
        self.assertEqual(self.new_credential.password, "123456")






if __name__ == "__main__":
    unittest.main()