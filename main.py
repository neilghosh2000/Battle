from classes.game import Person, BColors

magic = [{"Spell": "Fire", "Cost": 100, "Damage": 120},
         {"Spell": "Thunder", "Cost": 90, "Damage": 100},
         {"Spell": "Blizzard", "Cost": 120, "Damage": 125}]
player1 = Person(1000, 450, 80, 60, magic)

for i in range(0, 5):
    print(player1.get_damage())

for j in range(0, 3):
    print(j)
    for i in range(0, 3):
        print(player1.get_magic_damage(i))
