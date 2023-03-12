#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test the Dice class."""

import unittest
from src.dice.dice import Dice


class TestDice(unittest.TestCase):
    """Test Dice."""

    def test_roll(self):
        """Test if rolling gives correct value."""
        dice = Dice()

        res = dice.roll([1, 1, 1, 1])
        exp = {'cast': (1, 1), 'sum': 2}

        self.assertEqual(res, exp)
