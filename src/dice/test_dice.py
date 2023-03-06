"""Test Dice"""
import unittest


class TestDice(unittest.TestCase):
    def test_roll(self):
        d = Dice()
        for _ in range(100):
            roll = d.roll()
            self.assertGreaterEqual(roll, 1)
            self.assertGreaterEqual(roll, 6)


