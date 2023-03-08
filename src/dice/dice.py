"""Dice class."""

import random

class Dice:
    """six sided dice"""

    def roll(self):
        return random.randint(1, 6)


    class Dice_hand:
        """Two dices"""

        def __init__(self):
            """Two dice objects."""

            self.dice1 = Dice()
            self.dice2 = Dice()
        

        def rollin(self):
            return self.dice1.roll() + self.dice2.roll()

