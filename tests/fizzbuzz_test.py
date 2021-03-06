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

    def test_fizzbuzz_10_returns_buzz(self):
        self.assertEqual('buzz', fizz_buzz(10))

    def test_fizzbuzz_15_returns_fizzbuzz(self):
        self.assertEqual('fizzbuzz', fizz_buzz(15))

    def test_fizzbuzz_30_returns_fizzbuzz(self):
        self.assertEqual('fizzbuzz', fizz_buzz(30))

    # 0
    def test_fizzbuzz_0_returns(self):
        self.assertEqual('invalid number 0', fizz_buzz(0))

    def test_fizzbuzz_negative3_returns_fizz(self):
        self.assertEqual('fizz', fizz_buzz(-3))

 # -number
    def test_fizzbuzz_negative1_returns_negative1(self):
        self.assertEqual('-1', fizz_buzz(-1))
    
    # not int
    def test_fizzbuzz_blah_returns_blah(self):
        self.assertEqual("invalid input blah, <class 'str'> is not a whole number", fizz_buzz('blah'))
    # floats
    def test_fizzbuzz_3_0_returns_invalid(self):
        self.assertEqual("invalid input 3.0, <class 'float'> is not a whole number", fizz_buzz(3.0))
    # strings
    # bool

    def test_fizzbuzz_none_returns_invalid(self):
        self.assertEqual("invalid input None, <class 'NoneType'> is not a whole number", fizz_buzz(None))
