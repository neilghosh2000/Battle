import random


class BColors:
    END = '\033[0m'

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'


class Person:
    def __init__(self, hp, mp, atk, dfn, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.dfn = dfn
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def get_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, i):
        self.mp -= self.magic[i].cost

    def choose_action(self):
        print(BColors.BOLD + BColors.CYAN + "Choose Action:" + BColors.END)
        i = 1
        for item in self.actions:
            print("     " + str(i), ":", item)
            i += 1

    def choose_magic_spell(self):
        print(BColors.BOLD + BColors.CYAN + "Choose Magic Spell:" + BColors.END)
        i = 1
        for spell in self.magic:
            print("     " + str(i) + " : " + spell.name + " (Cost : " + str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        print(BColors.BOLD + BColors.CYAN + "Choose Item:" + BColors.END)
        i = 1
        for item in self.items:
            print("     " + str(i) + " : " + item.name + " - " + item.description)
            i += 1












