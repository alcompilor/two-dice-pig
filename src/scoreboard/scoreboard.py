""""Scoreboard module."""


class Scoreboard:
    """Scoreboard Class."""

    def __init__(self):
        self.scores = {1: 0, 2: 0}

    def update_score(self, player, points):
        """"Update score."""
        if player not in self.scores:
            raise ValueError(f'Invalid player: {player}')
        self.scores[player] += points

    def get_score(self, player):
        """Get the score."""
        if player not in self.scores:
            raise ValueError(f'Invalid player: {player}')
        return self.scores[player]

    def print_scores(self):
        """Show the score."""
        print(f"Player 1: {self.scores[1]}")
        print(f"Player 2: {self.scores[2]}")


scoreboard = Scoreboard()
scoreboard.update_score(1, 5)
scoreboard.update_score(2, 5)
scoreboard.print_scores()
