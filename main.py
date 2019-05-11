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
elixir = Items("Elixir", "Heal", "Regenerates full HP and MP", 10000)
grenade = Items("Grenade", "Damage", "Deals 150 damage", 150)
trap = Items("Trap", "Damage", "Deals 90 damage", 90)

magic = [fire, thunder, blizzard, meteor, earthquake, cure, cura]
items = [{"name": small_potion, "quantity": 3}, {"name": large_potion, "quantity": 2}, {"name": elixir, "quantity": 1}
         , {"name": grenade, "quantity": 2}, {"name": trap, "quantity": 1}]

# Defining Player and Enemy
player1= Person("Player 1", 1000, 450, 80, 60, magic, items)
player2= Person("Player 2", 1000, 450, 80, 60, magic, items)
player3= Person("Player 3", 1000, 450, 80, 60, magic, items)
enemy = Person("Enemy   ", 800, 500, 90, 70, [], [])

players = [player1, player2, player3]
running = True

print(BColors.BOLD + BColors.RED + "Battle Begins!" + BColors.END)
while running:
    print("------------------------------------------------------------------------------------------------------------"
          "----------" + "\n")

    print("  " + BColors.BOLD + BColors.UNDERLINE + "Name" + BColors.END + "                                            "
             "    " + BColors.BOLD + BColors.UNDERLINE + "Health Points" + BColors.END + "                              "
             "      " + BColors.BOLD + BColors.UNDERLINE + "Magic Points" + BColors.END)

    for player in players:
        player.show_stats()

    for player in players:
        player.choose_action()
        choice = int(input("Please enter your choice:" + "\n"))

        # If player chooses Attack
        if choice == 1:
            player_damage = player.get_damage()
            enemy.hp -= player_damage
            print("\n" + BColors.GREEN + player.name + "attacked the enemy for", player_damage, "points." + BColors.END)

        # If the player chooses Magic
        elif choice == 2:
            player.choose_magic_spell()
            magic_choice = int(input("Please enter your choice:" + "\n")) - 1

            if magic_choice == -1:
                continue

            magic_cost = magic[magic_choice].cost
            magic_damage = magic[magic_choice].damage

            if player.get_mp() >= magic_cost:
                if magic[magic_choice].category == "White":
                    player.hp += magic_damage
                    player.reduce_mp(magic_choice)

                    if player.get_hp() >= player.get_max_hp():
                        magic_damage -= (player.get_hp() - player.get_max_hp())
                        player.hp = player.get_max_hp()
                    print("\n" + BColors.GREEN + player.name + " healed yourself using " + magic[magic_choice].name + ", using " +
                          str(magic_cost) + " magic points for " + str(magic_damage) +
                          " health." + BColors.END)

                elif magic[magic_choice].category == "Black":
                    player.reduce_mp(magic_choice)
                    enemy.hp -= magic_damage
                    print("\n" + BColors.BLUE + player.name + " attacked the enemy using " + magic[magic_choice].name +
                          ", using " + str(magic_cost) + " magic points and dealing " + str(magic_damage) + " damage."
                          + BColors.END)

            elif player.get_mp() < magic_cost:
                print("\n" + BColors.RED + player.name + "does not have enough magic points to perform this spell!" +
                      BColors.END + "\n")
                continue

        # If the player choose Items
        elif choice == 3:
            player.choose_item()
            item_choice = int(input("Please enter your choice:" + "\n")) - 1
            item_value = player.items[item_choice]["name"].value

            if item_choice == -1:
                continue

            if player.items[item_choice]["quantity"] > 0:
                player.items[item_choice]["quantity"] -= 1

                if player.items[item_choice]["name"].category == "Heal":
                    player.hp += item_value
                    if player.items[item_choice]["name"].name == "Elixir":
                        mp_value = player.get_max_mp() - player.get_mp()
                        player.mp = player.get_max_mp()

                    if player.get_hp() >= player.get_max_hp():
                        item_value -= (player.get_hp() - player.get_max_hp())
                        player.hp = player.get_max_hp()

                    if player.items[item_choice]["name"].name == "Elixir":
                        print("\n" + BColors.YELLOW + player.name + " healed yourself using " + items[item_choice][
                            "name"].name + " for " + str(item_value) + " HP and " + str(mp_value) + " MP." +
                              BColors.END)
                    else:
                        print("\n" + BColors.YELLOW + player.name + " healed yourself using " +
                              items[item_choice]["name"].name + " for " + str(item_value) + " HP." + BColors.END)

                elif items[item_choice]["name"].category == "Damage":
                    enemy.hp -= item_value
                    print(BColors.YELLOW + player.name + " attacked the enemy using " + items[item_choice]["name"].name
                          + " for " + str(item_value) + " HP." + BColors.END)
            else:
                print(BColors.RED + "Selected Item not available!" + BColors.END)
                continue
        else:
            continue

        enemy_damage = enemy.get_damage()
        player.hp -= enemy_damage
        print(BColors.RED + "The enemy attacked " + player.name + " for " + str(enemy_damage) + " points." + BColors.END
              + "\n")

        if player.get_hp() <= 0:
            player.hp = 0
            running = False
        elif enemy.get_hp() <= 0:
            enemy.hp = 0
            running = False

        print(BColors.RED + "Enemy's HP : " + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + BColors.END)

        if player.get_hp() == 0:
            print(BColors.RED + "The Enemy has won!" + BColors.END)
        elif enemy.get_hp() == 0:
            print(BColors.GREEN + "The Enemy has been defeated!" + BColors.END)

