class Bowling():

    # Símbolos que representan tiradas especiales.
    symbs = "X-/"

    def __init__(self, scorecard):
        self.scorecard = []
        roll = 1
        for c in scorecard:
            frame = []
            if c not in symbs:
                if len(frame) != 2:
                    frame.append(c)
                else:
                    self.scorecard.append(frame)

    def game_score(self):
