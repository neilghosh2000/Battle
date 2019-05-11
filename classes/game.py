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

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, i):
        self.mp -= self.magic[i]["Cost"]

    def get_spell_cost(self, i):
        return self.magic[i]["Cost"]

    def get_spell_name(self, i):
        return self.magic[i]["Spell"]

    def choose_action(self):
        print("Choose Action:")
        i = 1
        for item in self.actions:
            print(str(i), ":", item)
            i += 1

    def choose_magic_spell(self):
        print("Choose Magic Spell:")
        i = 1
        for spell in self.magic:
            print(str(i) + " : " + spell["Spell"] + " (Cost : " + str(spell["Cost"]) + ")")
            i += 1












