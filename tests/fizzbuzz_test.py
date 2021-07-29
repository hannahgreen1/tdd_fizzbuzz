import unittest
from src.fizzbuzz import *

class TestFizzbuzz(unittest.TestCase):
    
    def test_fizzbuzz_1_return_1(self):
        self.assertEqual('1', fizz_buzz(1))