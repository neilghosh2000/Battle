from classes.game import Person, BColors
from classes.magic import Spell
from classes.items import Items


# Defining White Magic Spells
fire = Spell("Fire", 100, 120, "Black")
thunder = Spell("Thunder", 90, 100, "Black")
blizzard = Spell("Blizzard", 120, 125, "Black")
meteor = Spell("Meteor", 75, 110, "Black")
earthquake = Spell("Earthquake", 95, 150, "Black")

# Defining Black Magic Spells
cure = Spell("Cure", 80, 100, "White")
cura = Spell("Cura", 110, 135, "White")

# Defining Items
small_potion = Items("Small Potion", "Heal", "Heals for 75 HP", 75)
large_potion = Items("Large Potion", "Heal", "Heals for 150 HP", 150)
elixir = Items("Elixir", "Heal", "Regenerates full HP", 10000)
grenade = Items("Grenade", "Damage", "Deals 150 damage", 150)
trap = Items("Trap", "Damage", "Deals 90 damage", 90)

magic = [fire, thunder, blizzard, meteor, earthquake, cure, cura]
items = [small_potion, large_potion, elixir, grenade, trap]

# Defining Player and Enemy
player = Person(1000, 450, 80, 60, magic, items)
enemy = Person(800, 500, 90, 70, [], [])

running = True

print(BColors.BOLD + BColors.RED + "Battle Begins!" + BColors.END)
while running:
    print("==============================================")
    player.choose_action()
    choice = int(input("Please enter your choice:" + "\n"))

    if choice == 1:
        player_damage = player.get_damage()
        enemy.hp -= player_damage
        print("\n" + BColors.GREEN + "You attacked the enemy for", player_damage, "points." + BColors.END)

    elif choice == 2:
        player.choose_magic_spell()
        magic_choice = int(input("Please enter your choice:" + "\n")) - 1
        magic_cost = magic[magic_choice].cost
        magic_damage = magic[magic_choice].damage

        if player.get_mp() >= magic_cost:
            if magic[magic_choice].category == "White":
                player.hp += magic_damage
                player.reduce_mp(magic_choice)

                if player.get_hp() >= player.get_max_hp():
                    magic_damage -= (player.get_hp() - player.get_max_hp())
                    player.hp = player.get_max_hp()
                print("\n" + BColors.GREEN + "You healed yourself using " + magic[magic_choice].name + ", using " +
                      str(magic_cost) + " magic points for " + str(magic_damage) +
                      " health." + BColors.END)

            elif magic[magic_choice].category == "Black":
                player.reduce_mp(magic_choice)
                enemy.hp -= magic_damage
                print("\n" + BColors.BLUE + "You attacked the enemy using " + magic[magic_choice].name + ", using "
                      + str(magic_cost) + " magic points and dealing " + str(magic_damage) + " damage." + BColors.END)

        elif player.get_mp() < magic_cost:
            print("\n" + BColors.RED + "You do not have enough magic points to perform this spell!" + BColors.END + "\n")
            continue

    elif choice == 3:
        player.choose_item()
        item_choice = int(input("Please enter your choice:" + "\n")) - 1
        item_value = items[item_choice].value

        if items[item_choice].category == "Heal":
            player.hp += item_value
            if player.get_hp() >= player.get_max_hp():
                item_value -= (player.get_hp() - player.get_max_hp())
                player.hp = player.get_max_hp()
            print("\n" + BColors.YELLOW + "You healed yourself using " + items[item_choice].name + " for " +
                  str(item_value) + " HP." + BColors.END)

        elif items[item_choice].category == "Damage":
            enemy.hp -= item_value
            print(BColors.YELLOW + "You attacked the enemy using " + items[item_choice].name + " for " +
                  str(item_value) + " HP." + BColors.END)

    enemy_damage = enemy.get_damage()
    player.hp -= enemy_damage
    print(BColors.RED + "The enemy attacked you for " + str(enemy_damage) + " points." + BColors.END + "\n")

    if player.get_hp() <= 0:
        player.hp = 0
        running = False
    elif enemy.get_hp() <= 0:
        enemy.hp = 0
        running = False

    print(BColors.RED + "Your Enemy's HP : " + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + BColors.END)
    print(BColors.GREEN + "Your HP : " + str(player.get_hp()) + "/" + str(player.get_max_hp()) + BColors.END)
    print(BColors.BLUE + "Your MP : " + str(player.get_mp()) + "/" + str(player.get_max_mp()) + BColors.END + "\n")

    if player.get_hp() == 0:
        print(BColors.RED + "Your Enemy has defeated you!" + BColors.END)
    elif enemy.get_hp() == 0:
        print(BColors.GREEN + "You have defeated your enemy!" + BColors.END)

