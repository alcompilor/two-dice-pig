"""Scoreboard module."""


class Scoreboard:
    """Scoreboard Class."""

    def __init__(self):
        """Create the new high score."""
        self.max_score = 100
        self.winner = None
        self.scores = []
    
    def add_players(self, players_list):
        for player in players_list:
            self.scores.append([player, 0])


    def update_score(self, name, score):
        """Add a new score to the list."""
        for i in range(0, len(self.scores)-1):
            if name in self.scores[i][0]:
                self.scores[i][1] = score
    
    
    def reset_score(self, name):
        for i in range(0, len(self.scores)-1):
            if name in self.scores[i][0]:
                self.scores[i][1] = 0
    
    def get_winner(self):
        for score_list in self.scores:
            if score_list[1] == 100:
                self.winner = score_list[0]
                return self.winner
            else:
                return None
    

    def get_player(self, name):
        for score_list in self.scores:
           if score_list[0] == name:
               return score_list

