class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        
        return score_situation(self.player1_score, self.player2_score)


def score_situation(player1_score, player2_score):
    score = ""

    if player1_score == player2_score:
        score = equal_score_shout(player1_score)

    elif player1_score >= 4 or player2_score >= 4:
        score = advantage_score_shout(player1_score, player2_score)
    else:
        score = score_shout(player1_score)
        score += "-"
        score += score_shout(player2_score)
    
    return score

def equal_score_shout(players_score):
        
    if players_score == 0: 
        return "Love-All"
    elif players_score == 1:
        return "Fifteen-All"
    elif players_score == 2:
        return "Thirty-All"
    else:
        return "Deuce"

def advantage_score_shout(player1_score, player2_score):

    minus_result = player1_score - player2_score

    if minus_result == 1:
        return "Advantage player1"
    elif minus_result == -1:
        return "Advantage player2"
    elif minus_result >= 2:
        return "Win for player1"
    else:
        return "Win for player2"

def score_shout(player_score):

    if player_score == 0:
        return  "Love"
    elif player_score == 1:
        return "Fifteen"
    elif player_score == 2:
        return  "Thirty"
    elif player_score == 3:
        return  "Forty"


