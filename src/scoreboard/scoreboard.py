""""Scoreboard module."""


class Scoreboard:
    """Scoreboard Class."""

    def __init__(self,max_scores=10):
        """Create the new high score."""
        self.max_scores = max_scores
        self.scores = []

    def add_score(self, name, score):
        """Add a new score to the list."""
        self.scores.append((name, score))
        self.scores.sort(reverse=True, key=lambda x: x[1])
        self.scores = self.scores[:self.max_scores]

    def __str__(self):
        """Return a string representation of the high score."""
        lines = ["HIGH SCORES:"]
        for i, (name, score) in enumerate(self.scores):
            lines.append(f"{i+1}. {name}: {score}")
        return "\n".join(lines)

