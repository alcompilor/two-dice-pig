#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import computer


class TestComputer(unittest.TestCase):
    """Testing computer class."""

    def test_init(self):
        """Tests constructor of the computer class."""
        comp = computer.Computer(3)  # testing with good value

        res1 = comp.get_difficulty()
        exp1 = 3

        res2 = comp.get_probability()
        exp2 = (10, 10, 10, 30, 20, 20)

        res3 = comp.get_biased_list()
        exp3 = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6]

        comp2 = computer.Computer(4)  # testing with bad value

        res4 = comp2.get_difficulty()
        exp4 = 1

        res5 = comp2.get_probability()
        exp5 = (20, 30, 20, 10, 10, 10)

        res6 = comp2.get_biased_list()
        exp6 = [1, 1, 2, 2, 2, 3, 3, 4, 5, 6]

        self.assertEqual(res1, exp1)
        self.assertEqual(res2, exp2)
        self.assertEqual(res3, exp3)

        self.assertEqual(res4, exp4)
        self.assertEqual(res5, exp5)
        self.assertEqual(res6, exp6)

    def test_get_difficulty(self):
        """Fetches value of difficulty variable and tests if it's correct."""
        comp = computer.Computer(2)
        res = comp.get_difficulty()
        exp = 2

        self.assertEqual(res, exp)

    def test_set_difficulty(self):
        """Sets difficulty and verifies it."""
        comp = computer.Computer(1)
        comp.set_difficulty(2)
        res = comp.get_difficulty()
        exp = 2

        self.assertEqual(res, exp)

    def test_set_probability(self):
        """Test setting the probability of getting each dice face."""
        comp = computer.Computer(1)
        comp.set_probability()

        res = comp.get_probability()
        exp = (20, 30, 20, 10, 10, 10)

        self.assertEqual(res, exp)

    def test_get_probability(self):
        """Fetches value of probability variable and tests if it's correct."""
        comp = computer.Computer(1)
        res = comp.get_probability()
        exp = (20, 30, 20, 10, 10, 10)

        self.assertEqual(res, exp)

    def test_generate_biased_list(self):
        """Generate biased dice faces list based on probability & verify it."""
        comp = computer.Computer(1)
        res = comp.generate_biased_list()
        exp = [1, 1, 2, 2, 2, 3, 3, 4, 5, 6]

        self.assertEqual(res, exp)

    def test_get_biased_list(self):
        """Tests if biased list is fetched correctly."""
        comp = computer.Computer(2)

        res = comp.get_biased_list()
        exp = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
