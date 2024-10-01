import unittest
from unittest.mock import MagicMock
from bank_account import BankAccount, Current_interest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.test1 = BankAccount(1000, "test")
        self.test2 = BankAccount(2000, "test2")
        self.test3 = BankAccount(3000, "test3")
        self.invalidnum = "This is not right" # test data for non numeric values

    def tearDown(self):
        self.test1 = None
        self.test2 = None
        self.test3 = None

    def test_deposit(self):
        self.test1.deposit(200)
        self.assertEqual(self.test1.balance, 1200)

    def test_withdraw(self):
        self.test2.withdraw(200)
        self.assertEqual(self.test2.balance, 1800)

    def test_insufficient_funds(self):
        with self.assertRaises(Exception):
            self.test3.withdraw(4000)

    def test_interest(self):
        Current_interest.get_rate = MagicMock(return_value=0.02)
        interest = self.test1.compute_interest(Current_interest())
        self.assertEqual(interest, self.test1.balance * 0.02)

if __name__ == "__main__":
    unittest.main()