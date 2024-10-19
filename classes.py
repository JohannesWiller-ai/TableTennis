# classes.py

class Game:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player1 = 0
        self.score_player2 = 0
        self.winner = None
        self.history = []

    def add_point(self, player):
        if self.winner:
            return  # Do not add points if the game has ended
        if player == 1:
            self.score_player1 += 1
            self.history.append((1, 'add'))
        elif player == 2:
            self.score_player2 += 1
            self.history.append((2, 'add'))
        self.check_winner()

    def undo_last_action(self):
        if not self.history:
            return
        last_action = self.history.pop()
        player, action = last_action
        if action == 'add':
            if player == 1:
                self.score_player1 -= 1
            elif player == 2:
                self.score_player2 -= 1
        # Reset the winner and check if there's still a winner
        self.winner = None
        self.check_winner()

    def reset_game(self):
        self.score_player1 = 0
        self.score_player2 = 0
        self.winner = None
        self.history.clear()

    def check_winner(self):
        # Check for a winner based on the current scores
        if self.score_player1 >= 11 and self.score_player1 - self.score_player2 >= 2:
            self.winner = self.player1_name
        elif self.score_player2 >= 11 and self.score_player2 - self.score_player1 >= 2:
            self.winner = self.player2_name
        else:
            self.winner = None

    def is_player_at_match_point(self, player):
        if self.winner:
            return False  # Game is over

        if player == 1:
            player_score = self.score_player1
            opponent_score = self.score_player2
        else:
            player_score = self.score_player2
            opponent_score = self.score_player1

        # Calculate the required score to win
        required_score = max(11, opponent_score + 2)

        # Check if the player is one point away from winning
        if player_score == required_score - 1:
            return True
        else:
            return False
