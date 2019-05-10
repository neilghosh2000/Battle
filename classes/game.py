import random


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, dfn, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.dfn = dfn
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def get_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def get_magic_damage(self, i):
        mg = self.magic[i]["Damage"]
        return random.randrange(mg - 5, mg + 5)











