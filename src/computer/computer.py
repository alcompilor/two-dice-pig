#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Computer module implementing a simple concept to control its difficulty."""

from random import shuffle


class Computer:
    """Computer class."""

    def __init__(self, difficulty):
        """Init constructor for the computer class."""
        self.difficulty = difficulty if 0 < difficulty < 4 else 1
        self.probability = self.set_probability()
        self.biased_list = self.generate_biased_list()
        self.decision_list = self.generate_decision_list()

    def get_difficulty(self):
        """Fetch and return computer difficulty."""
        return self.difficulty

    def set_difficulty(self, difficulty):
        """Change the difficulty of the computer."""
        self.difficulty = difficulty

    def set_probability(self):
        """Implement dice faces probability based on difficulty."""
        match self.difficulty:
            case 1:
                self.probability = (20, 30, 20, 10, 10, 10)
            case 2:
                self.probability = (10, 20, 30, 10, 20, 10)
            case 3:
                self.probability = (10, 10, 10, 30, 20, 20)

        return self.get_probability()

    def get_probability(self):
        """Fetch and return dice faces probability."""
        return self.probability

    def generate_biased_list(self):
        """Generate biased list based on probability."""
        biased_list = []
        current_face = 0
        for i in self.get_probability():
            i = i // 10
            current_face += 1
            for _ in range(i):
                biased_list.append(current_face)
        shuffle(biased_list)
        return biased_list

    def get_biased_list(self):
        """Fetch and return biased list with dice faces."""
        return self.biased_list

    def generate_decision_list(self):
        """Generate decision list to pass or roll based on difficulty."""
        match(self.get_difficulty()):
            case 1:
                decision_list = ["pass", "pass", "roll", "roll", "roll"]
                shuffle(decision_list)
                return decision_list
            case 2:
                decision_list = ["pass", "roll", "roll", "roll"]
                shuffle(decision_list)
                return decision_list
            case 3:
                decision_list = ["pass", "roll", "roll",
                                 "roll", "roll", "roll"]
                shuffle(decision_list)
                return decision_list

    def get_decision_list(self):
        """Fetch and return decision list."""
        return self.decision_list
