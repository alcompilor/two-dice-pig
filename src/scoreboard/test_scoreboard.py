import unittest
from src.scoreboard.scoreboard  import Scoreboard

"""Test Scoreboard class"""

class ScoreboardTestCase(unittest.TestCase):

     """First test"""
    
    def test_add_score(self):
    
     """Try multiple numbers. """

     hs = HighScore(max_scores = 3)
     hs.add_score("Alex", 100)
     hs.add_score("Bob", 50)
     hs.add_score("Richard", 75)
     self.assertEqual(str(hs), "HIGH SCORES:\n1. Alex: 100 \n2. Richard: 75 \n3. Bob: 50 ") 
     hs.add_score("David", 90)
     self.assertEqual(str(hs), "HIGH SCORES: \n1. Alex:10 \n2. David: 90 \n3. Richard: 75")


if __name__ == "__main__":
    unittest.main()
