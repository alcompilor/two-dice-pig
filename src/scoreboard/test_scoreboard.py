import unittest
from scoreboard import Scoreboard

class ScoreboardTestCase(unittest.TestCase):
    def setUp(self):
        self.scoreboard = Scoreboard()

    def test_initial_scores(self):
        self.assertEqual(self.scoreboard.get_score(1), 0)
        self.assertEqual(self.scoreboard.get_score(2), 0)

    def test_update_score(self):
        self.scoreboard.update_score(1, 5)
        self.assertEqual(self.scoreboard.get_score(1), 5)
        self.scoreboard.update_score(2, 3)
        self.assertEqual(self.scoreboard.get_score(2), 3)

    def test_invalid_player(self):
         with self.assertRaises(ValueError):
                self.scoreboard.update_score(3, 10)
         with self.assertRaises(ValueError):
             self.scoreboard.get_score(3)


if __name__ == "__main__":
    unittest.main()

