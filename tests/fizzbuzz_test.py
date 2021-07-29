import unittest
from src.fizzbuzz import *

class TestFizzbuzz(unittest.TestCase):
    
    def test_fizzbuzz_1_return_1(self):
        self.assertEqual('1', fizz_buzz(1))

    def test_fizzbuzz_2_returns_2(self):
        self.assertEqual('2', fizz_buzz(2))

    def test_fizzbuzz_3_returns_fizz(self):
        self.assertEqual('fizz', fizz_buzz(3))

    def test_fizzbuzz_5_returns_buzz(self):
        self.assertEqual('buzz', fizz_buzz(5))

    def test_fizzbuzz_6_returns_fizz(self):
        self.assertEqual('fizz', fizz_buzz(6))