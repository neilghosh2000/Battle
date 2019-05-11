import random


class Spell:

    def __init__(self, name, cost, damage, category):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.category = category

    def get_magic_damage(self):
        return random.randrange(self.damage - 15, self.damage + 15)







