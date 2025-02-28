from register import register_page_validation
from login import login_validation
import unittest

class TestValidation(unittest.TestCase):
    #Function to check Register process by providing correct data
    def test_register_properly(self):
        self.assertTrue(register_page_validation("Rubina Pant","20", "rubina", "player"))

    #Function to check Register process by providing incorrect data
    def test_register_incorrect(self):
        self.assertRaises(ValueError,register_page_validation,"Rubina Pant","Twenty", "rubina", "player")

    #Function to check Signin process by providing correct data
    def test_signin_properly(self):
        self.assertTrue(login_validation("rubina","rubina"))

    #Function to check Signin process by providing incorrect data
    def test_signin_incorrect(self):
        self.assertRaises(ValueError, login_validation,"rubina","Rubina")

