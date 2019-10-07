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

if __name__ == "__main__":
    unittest.main()