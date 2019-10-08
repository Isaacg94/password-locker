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
        Method that will run before each test and creates a new instance of Credentials class before each test method is declared and stores it in an instance variable called self.new_contact
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
    
    def test_delete_credential(self):
        """
        Test to check if we can remove a credential from the credentials list
        """
        # self.new_credential.save_credential()
        # test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_display_credential(self):
        """
        Test to check if credentials can be displayed.
        """
        
        self.assertEqual(Credentials.display_credential(),Credentials.credentials_list)

    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from a credential
        '''

        self.new_credential.save_credential()
        Credentials.copy_password("123456")

        self.assertEqual(self.new_credential.password,pyperclip.paste())

if __name__ == "__main__":
    unittest.main()
