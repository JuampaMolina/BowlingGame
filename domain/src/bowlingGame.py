class Bowling():

    # Símbolos que representan tiradas especiales.
    GUTTERBALL = '-'
    SPARE = '/'
    STRIKE = 'X'

    LAST_FRAME = 10
    TOTAL_PINS = 10

    def __init__(self, scorecard):
        # Convertimos el string score_card en una lista.
        self.scorecard = list(scorecard)
        self.score = 0
        self.current_frame = 1
        self.current_roll = 0
        self.rolls_in_frame = 0
        self.extra_points = []
        self.previous_roll = 0

    def advance_roll(self):
        for roll in self.scorecard:
            if self.current_frame < 11:
                Bowling.game_score(self, roll)
                if len(self.extra_points) > 0:
                    Bowling.sum_extra_points(self)
            if roll.isdigit():
                self.previous_roll = int(roll)
            elif roll == Bowling.GUTTERBALL:
                self.previous_roll = 0
            elif roll == Bowling.SPARE or roll == Bowling.STRIKE:
                self.previous_roll = 10

        return self.score

    def game_score(self, roll):
        if roll.isdigit():
            Bowling.rollNormal(self, roll)
        elif roll == Bowling.GUTTERBALL:
            Bowling.rollGutterball(self)
        elif roll == Bowling.SPARE:
            Bowling.rollSpare(self, roll)
        elif roll == Bowling.STRIKE:
            Bowling.rollStrike(self, roll)

    def sum_extra_points(self):
        for roll in self.extra_points:
            if roll == Bowling.GUTTERBALL:
                self.score += 0
            elif roll == Bowling.STRIKE or roll == Bowling.SPARE:
                self.score += 10
            elif roll.isdigit():
                self.score += int(roll)
        self.extra_points = []

    def updateRolls(self):
        self.rolls_in_frame += 1
        self.current_roll += 1
        if self.rolls_in_frame == 2:
            self.current_frame += 1
            self.rolls_in_frame = 0

    def rollNormal(self, roll):
        Bowling.updateRolls(self)
        self.score += int(roll)

    def rollGutterball(self):
        Bowling.updateRolls(self)
        self.score += 0

    def rollSpare(self, roll):
        self.current_frame += 1
        self.rolls_in_frame = 0
        self.current_roll += 1
        self.extra_points = self.scorecard[self.current_roll:self.current_roll + 1]
        self.score += (10 - self.previous_roll)

    def rollStrike(self, roll):
        self.current_frame += 1
        self.rolls_in_frame = 0
        self.current_roll += 1
        self.extra_points = self.scorecard[self.current_roll:self.current_roll + 2]
        self.score += Bowling.TOTAL_PINS


if __name__ == "__main__":
    assert Bowling('26X3/4281X422/5/2/5').advance_roll() == 121
