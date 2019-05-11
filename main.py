from classes.game import Person, BColors
from classes.magic import Spell


# Defining White Magic Spells
fire = Spell("Fire", 100, 120, "Black")
thunder = Spell("Thunder", 90, 100, "Black")
blizzard = Spell("Blizzard", 120, 125, "Black")
meteor = Spell("Meteor", 105, 110, "Black")
earthquake = Spell("Earthquake", 135, 150, "Black")

# Defining Black Magic Spells
cure = Spell("Cure", 80, 100, "White")
cura = Spell("Cura", 110, 135, "White")

magic = [fire, thunder, blizzard, meteor, earthquake, cure, cura]
# Defining Player and Enemy
player = Person(1000, 450, 80, 60, magic)
enemy = Person(800, 500, 90, 70, [])

running = True

print(BColors.BOLD + BColors.FAIL + "Battle Begins!" + BColors.ENDC)
while running:
    print("==============================================")
    player.choose_action()
    choice = int(input("Please enter your choice:" + "\n"))

    if choice == 1:
        player_damage = player.get_damage()
        enemy.hp -= player_damage
        print(BColors.OKGREEN + "You attacked the enemy for", player_damage, "points." + BColors.ENDC)
    elif choice == 2:
        player.choose_magic_spell()
        magic_choice = int(input("Please enter your choice:" + "\n")) - 1
        magic_cost = magic[magic_choice].cost
        magic_damage = magic[magic_choice].damage

        if player.get_mp() >= magic_cost:
            if magic[magic_choice].category == "White":
                player.hp += magic_damage
                player.mp -= magic_cost
                if player.get_hp() >= player.get_max_hp():
                    magic_damage -= (player.get_hp() - player.get_max_hp())
                    player.hp = player.get_max_hp()
                print(BColors.OKGREEN + "You healed yourself using " + magic[magic_choice].name + ", using " +
                      str(magic_cost) + " magic points for " + str(magic_damage) +
                      " health." + BColors.ENDC)
            elif magic[magic_choice].category == "Black":
                player.mp -= magic_cost
                enemy.hp -= magic_damage
                print(BColors.OKBLUE + "You attacked the enemy using " + magic[magic_choice].name + ", using "
                      + str(magic_cost) + " magic points and dealing " + str(magic_damage) + " damage." + BColors.ENDC)
        elif player.get_mp() < magic_cost:
            print(BColors.FAIL + "You do not have enough magic points to perform this spell!" + BColors.ENDC + "\n")
            continue

    enemy_damage = enemy.get_damage()
    player.hp -= enemy_damage
    print(BColors.FAIL + "The enemy attacked you for", enemy_damage, "points." + BColors.ENDC + "\n")

    if player.get_hp() <= 0:
        player.hp = 0
        running = False
    elif enemy.get_hp() <= 0:
        enemy.hp = 0
        running = False

    print(BColors.FAIL + "Your Enemy's HP : " + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + BColors.ENDC)
    print(BColors.OKGREEN + "Your HP : " + str(player.get_hp()) + "/" + str(player.get_max_hp()) + BColors.ENDC)
    print(BColors.OKBLUE + "Your MP : " + str(player.get_mp()) + "/" + str(player.get_max_mp()) + BColors.ENDC + "\n")

    if player.get_hp() == 0:
        print(BColors.FAIL + "Your Enemy has defeated you!" + BColors.ENDC)
    elif enemy.get_hp() == 0:
        print(BColors.OKGREEN + "You have defeated your enemy!" + BColors.ENDC)

