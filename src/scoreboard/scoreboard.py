#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Scoreboard module."""


class Scoreboard:
    """Scoreboard Class."""

    def __init__(self, players_list):
        """Create the new high score."""
        self.max_score = 100
        self.winner = None
        self.scores = []
        for player in players_list:
            self.scores.append([player, 0])

    def update_score(self, name, score):
        """Add a new score to the list."""
        for i, _ in enumerate(self.scores):
            if name in self.scores[i][0]:
                self.scores[i][1] += score

    def reset_score(self, name):
        """Reset the score of players."""
        for i, _ in enumerate(self.scores):
            if name in self.scores[i][0]:
                self.scores[i][1] = 0

    def get_winner(self):
        """Get the winner."""
        for i, _ in enumerate(self.scores):
            if self.scores[i][1] >= 100:
                self.winner = self.scores[i][0]
                return self.winner
            else:
                return None

    def get_player(self, name):
        """Player getter."""
        for i, _ in enumerate(self.scores):
            if self.scores[i][0] == name:
                return self.scores[i]

    def get_scores(self):
        """Scores getter."""
        return self.scores
