class TennisGame2:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

def __init__(self, player1_name, player2_name):
    self.player1_name = player1_name
    self.player2_name = player2_name
    self.p1_points = 0
    self.p2_points = 0

def won_point(self, player_name):
    if player_name == self.player1_name:
        self.p1_points += 1
    elif player_name == self.player2_name:
        self.p2_points += 1

def score(self):
    if self.is_even():
        return self.even_score()

    if self.is_endgame():
        return self.endgame_score()

    return self.normal_score()

def is_even(self):
    return self.p1_points == self.p2_points

def is_endgame(self):
    return self.p1_points >= 4 or self.p2_points >= 4

def even_score(self):
    if self.p1_points < 3:
        return f"{self.SCORE_NAMES[self.p1_points]}-All"
    return "Deuce"

def endgame_score(self):
    diff = self.p1_points - self.p2_points

    if diff == 1:
        return f"Advantage {self.player1_name}"
    if diff == -1:
        return f"Advantage {self.player2_name}"
    if diff >= 2:
        return f"Win for {self.player1_name}"
    return f"Win for {self.player2_name}"

def normal_score(self):
    return f"{self.SCORE_NAMES[self.p1_points]}-{self.SCORE_NAMES[self.p2_points]}"

def set_p1_score(self, number):
    self.p1_points += number

def set_p2_score(self, number):
    self.p2_points += number

