#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test the Scoreboard class."""

import unittest
from src.scoreboard.scoreboard import Scoreboard


class ScoreboardTestCase(unittest.TestCase):
    """Test name and scores."""

    def test_scoreboard(self):
        """Create a scoreboard with two players."""
        players = ["Mohamed", "Ahmed"]
        scoreboard = Scoreboard(players)

        assert scoreboard.get_scores() == [["Mohamed", 0], ["Ahmed", 0]]

        scoreboard.update_score("Mohamed", 10)

        assert scoreboard.get_player("Mohamed") == ["Mohamed", 10]
        scoreboard.update_name("Mohamed", "Richard")
        assert scoreboard.get_player("Richard") == ["Richard", 10]

        scoreboard.reset_score("Richard")
        assert scoreboard.get_player("Richard") == ["Richard", 0]

        scoreboard.update_score("Richard", 100)
        assert scoreboard.get_winner() == "Richard"


if __name__ == "__main__":
    unittest.main()
