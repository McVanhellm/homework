from random import randint
class Coin():
    def __init__(self, one_side = 1, sec_side = 2):
        self.one_side = one_side
        self.sec_side = sec_side
    def roll(self):
        return randint(self.one_side, self.sec_side)