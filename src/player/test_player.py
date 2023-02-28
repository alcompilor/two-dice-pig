#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import player


class TestPlayer(unittest.TestCase):
    """Testing Player class."""

    def test_init(self):
        """Test the constuctor for the class."""
        player1 = player.Player("Computer", False)

        res1 = player1.get_name()
        exp1 = "Computer"
        res2 = player1.is_computer()

        player2 = player.Player("Sarah", True)

        res3 = player2.get_name()
        exp3 = "Sarah"

        res4 = player2.is_computer()

        self.assertEqual(res1, exp1)
        self.assertFalse(res2)

        self.assertEqual(res3, exp3)
        self.assertTrue(res4)

    def test_is_computer(self):
        """Test method that validates whether a player is a computer or not."""
        player1 = player.Player("Ahmed", False)
        res1 = player1.is_computer()

        player2 = player.Player("Computer", True)
        res2 = player2.is_computer()

        self.assertFalse(res1)
        self.assertTrue(res2)

    def test_get_name(self):
        """Test to fetch and return correct name for player."""
        player1 = player.Player("SomeName", False)
        res1 = player1.get_name()
        exp1 = "SomeName"

        player2 = player.Player(123, False)
        res2 = player2.get_name()
        exp2 = "123"

        self.assertEqual(res1, exp1)
        self.assertEqual(res2, exp2)

    def test_set_name(self):
        """Test method to set a correct name for player."""
        player1 = player.Player("HelloWorld", False)
        player1.set_name("RealName")

        res = player1.get_name()
        exp = "RealName"

        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
