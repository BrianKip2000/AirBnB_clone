#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test User class"""
    def TearUp(self):
        test_user = User()
    def TearDown(self):
        pass

    def test_user_attr(self):
        test_user = User()
        self.assertIs(test_user.email, "")
        self.assertIs(test_user.password, "")
        self.assertIs(test_user.first_name, "")
        self.assertIs(test_user.last_name, "")

if __name__ == "__main__":
    TestUser().unittest()

