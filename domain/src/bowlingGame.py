class Bowling():

    # Símbolos que representan tiradas especiales.
    GUTTERBALL = '-'
    SPARE = '/'
    STRIKE = 'X'

    LAST_FRAME = 10
    TOTAL_PINS = 10

    def __init__(self, scorecard):
        # Convertimos el string score_card en una lista.
        self.scorecard = scorecard
        self.score = 0
        self.current_frame = 1
        self.current_roll = 0
        self.rolls_in_frame = 0
        self.special = 0

    def game_score(self):
        for roll in self.scorecard:
            if self.current_frame < self.LAST_FRAME:
                if self.special > 0:
                    self.special -= 1
                    if roll == Bowling.GUTTERBALL:
                        self.score += 0
                    if roll == Bowling.STRIKE or roll == Bowling.SPARE:
                        self.score += 10
                    if roll.isdigit():
                        self.score += int(roll)
                if roll.isdigit():
                    Bowling.rollNormal(self, roll)
                if roll == Bowling.GUTTERBALL:
                    Bowling.rollGutterball(self)
                if roll == Bowling.SPARE:
                    Bowling.rollSpare(self)
                if roll == Bowling.STRIKE:
                    Bowling.rollStrike(self)

        return self.score

    def rollDone(self):
        self.rolls_in_frame += 1
        if self.rolls_in_frame == 2:
            self.current_frame += 1
            self.rolls_in_frame = 0

    def rollNormal(self, score):
        Bowling.rollDone(self)
        self.current_roll += 1
        self.score += int(score)

    def rollGutterball(self):
        Bowling.rollDone(self)
        self.score += 0

    def rollSpare(self):
        self.current_frame += 1
        Bowling.rollDone(self)
        self.score += 10
        self.special += 1

    def rollStrike(self):
        self.current_frame += 1
        Bowling.rollDone(self)
        self.score += 10
        self.special = 2
