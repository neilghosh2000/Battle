import random


class BColors:
    END = '\033[0m'

    BLACK = '\033[30m'
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
    def __init__(self, name, hp, mp, atk, dfn, magic, items):
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
        self.name = name

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
        print("\n" + BColors.BOLD + BColors.MAGENTA + self.name + ":" + BColors.END)
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
            print("     " + str(i) + " : " + item["name"].name + " - " + item["name"].description + " (x" +
                  str(item["quantity"]) + ")")
            i += 1

    @staticmethod
    def choose_target(enemies):
        print(BColors.BOLD + BColors.RED + "Choose Target:" + BColors.END)
        i = 1
        for enemy in enemies:
            print("     " + str(i) + " : " + enemy.name)
            i += 1
        return int(input("Please choose your target:")) - 1

    def show_enemy_stats(self):
        hp_bar = ""
        hp_bar_invisible = ""
        hp_bar_length = round((self.get_hp() / self.get_max_hp()) * 50)
        while len(hp_bar) < hp_bar_length:
            hp_bar += "█"
        while len(hp_bar_invisible) < 50 - hp_bar_length:
            hp_bar_invisible += "█"

        hp_blank = ""
        hp_blank_length = len(str(self.get_hp()))
        while hp_blank_length < len(str(self.get_max_hp())):
            hp_blank += " "
            hp_blank_length += 1

        print(BColors.BOLD + self.name + ":" + "                       " + hp_blank + str(self.get_hp()) + "/" +
              str(self.get_max_hp()) + " |" + BColors.END + BColors.RED + hp_bar + BColors.END + BColors.BLACK +
              hp_bar_invisible + BColors.END + BColors.BLACK + BColors.BOLD + "|" + BColors.END)

    def show_stats(self):
        hp_bar = ""
        hp_bar_invisible = ""
        hp_bar_length = round((self.get_hp() / self.get_max_hp()) * 25)
        while len(hp_bar) < hp_bar_length:
            hp_bar += "█"
        while len(hp_bar_invisible) < 25 - hp_bar_length:
            hp_bar_invisible += "█"

        mp_bar = ""
        mp_bar_invisible = ""
        mp_bar_length = round((self.get_mp() / self.get_max_mp()) * 10)
        while len(mp_bar) < mp_bar_length:
            mp_bar += "█"
        while len(mp_bar_invisible) < 10 - mp_bar_length:
            mp_bar_invisible += "█"

        hp_blank = ""
        mp_blank = ""
        hp_blank_length = len(str(self.get_hp()))
        mp_blank_length = len(str(self.get_mp()))
        while hp_blank_length < len(str(self.get_max_hp())):
            hp_blank += " "
            hp_blank_length += 1
        while mp_blank_length < len(str(self.get_max_mp())):
            mp_blank += " "
            mp_blank_length += 1

        print(BColors.BOLD + self.name + ":" + "                     " + hp_blank + str(self.get_hp()) + "/" +
              str(self.get_max_hp()) + " |" + BColors.END + BColors.GREEN + hp_bar + BColors.END + BColors.BLACK +
              hp_bar_invisible + BColors.END + BColors.BLACK + BColors.BOLD + "|            " + mp_blank +
              str(self.get_mp()) + "/" + str(self.get_max_mp()) + "|" + BColors.END + BColors.BLUE + mp_bar +
              BColors.END + BColors.BLACK + mp_bar_invisible + BColors.END + BColors.BLACK + "|" + BColors.END)












