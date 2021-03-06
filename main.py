from classes.game import Person, BColors
from classes.magic import Spell
from classes.items import Items
import random


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
enemy_magic = [fire, thunder, meteor, cura]
items = [{"name": small_potion, "quantity": 3}, {"name": large_potion, "quantity": 2}, {"name": elixir, "quantity": 1}
         , {"name": grenade, "quantity": 2}, {"name": trap, "quantity": 1}]

# Defining Players and Enemies
player1 = Person("Player 1", 1000, 450, 10, 60, magic, items)
player2 = Person("Player 2", 1000, 450, 10, 60, magic, items)
player3 = Person("Player 3", 1000, 450, 10, 60, magic, items)
enemy1 = Person("Enemy 1", 800, 500, 90, 70, enemy_magic, [])
enemy2 = Person("Enemy 2", 800, 500, 90, 70, enemy_magic, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2]
running = True

print(BColors.BOLD + BColors.RED + "Battle Begins!" + BColors.END)
while running:
    print("------------------------------------------------------------------------------------------------------------"
          "----------" + "\n")

    print("  " + BColors.BOLD + BColors.UNDERLINE + "Name" + BColors.END + "                                            "
             "    " + BColors.BOLD + BColors.UNDERLINE + "Health Points" + BColors.END + "                              "
             "      " + BColors.BOLD + BColors.UNDERLINE + "Magic Points" + BColors.END)

    # Show stats for all remaining players and enemies
    for player in players:
        player.show_stats()
    print()
    for enemy in enemies:
        enemy.show_enemy_stats()

    # Player attack phase
    i = 0
    while i < len(players):
        player = players[i]
        player.choose_action()
        choice = int(input("Please enter your choice:" + "\n"))

        # If player chooses Attack
        if choice == 1:
            player_damage = player.get_damage()
            player_target = player.choose_target(enemies)
            enemies[player_target].hp -= player_damage
            print("\n" + BColors.GREEN + player.name + " attacked " + enemies[player_target].name + " for",
                  player_damage, "points." + BColors.END)

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
                    player_target = player.choose_target(enemies)
                    enemies[player_target].hp -= magic_damage
                    print("\n" + BColors.BLUE + player.name + " attacked " + enemies[player_target].name + " using " +
                          magic[magic_choice].name + ", using " + str(magic_cost) + " magic points and dealing " +
                          str(magic_damage) + " damage." + BColors.END)

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
                    player_target = player.choose_target(enemies)
                    enemies[player_target].hp -= item_value
                    print(BColors.YELLOW + player.name + " attacked " + enemies[player_target].name + " using " +
                          items[item_choice]["name"].name + " for " + str(item_value) + " HP." + BColors.END)
            else:
                print(BColors.RED + "Selected Item not available!" + BColors.END)
                continue
        else:
            continue

        i += 1

    # Checking if player is alive
    for player in players:
        if player.get_hp() <= 0:
            player.hp = 0
            print(BColors.RED + BColors.BOLD + player.name + " has died!" + BColors.END)
            players.remove(player)

    # Checking if enemy is alive
    for enemy in enemies:
        if enemy.get_hp() <= 0:
            enemy.hp = 0
            print(BColors.GREEN + BColors.BOLD + enemy.name + " has been defeated!" + BColors.END)
            enemies.remove(enemy)

    # Checking number of remaining players and enemies
    players_remaining = len(players)
    enemies_remaining = len(enemies)

    if players_remaining == 0:
        print(BColors.BOLD + BColors.RED + "The Enemies have defeated you!" + BColors.END)
    elif enemies_remaining == 0:
        print(BColors.BOLD + BColors.GREEN + "You have won!" + BColors.END)

    # Enemy attack phase
    print()
    for enemy in enemies:
        enemy_choice = random.randrange(1, 3)

        # If enemy chooses magic
        if enemy_choice == 2:
            magic_choice = random.randrange(0, len(enemy.magic))
            magic_cost = magic[magic_choice].cost
            magic_damage = magic[magic_choice].damage

            if enemy.get_mp() >= magic_cost:
                per = enemy.get_hp() / enemy.get_max_hp() * 100

                # Enemy only uses white magic if his health is less than 50%
                if magic[magic_choice].category == "White" and per <= 50:
                    enemy.hp += magic_damage
                    enemy.reduce_mp(magic_choice)

                    if enemy.get_hp() >= enemy.get_max_hp():
                        magic_damage -= (enemy.get_hp() - enemy.get_max_hp())
                        enemy.hp = enemy.get_max_hp()
                    print(BColors.RED + enemy.name + " healed himself using " + magic[magic_choice].name + ", using " +
                          str(magic_cost) + " magic points for " + str(magic_damage) +
                          " health." + BColors.END)

                # Enemy uses black magic otherwise
                else:
                    enemy.reduce_mp(magic_choice)
                    enemy_target = random.randrange(0, len(players))
                    players[enemy_target].hp -= magic_damage
                    print(BColors.RED + enemy.name + " attacked " + players[enemy_target].name + " using " +
                          magic[magic_choice].name + ", using " + str(magic_cost) + " magic points and dealing " +
                          str(magic_damage) + " damage." + BColors.END)
            else:
                enemy_choice = 1

        # If enemy chooses to attack
        if enemy_choice == 1:
            enemy_damage = enemy.get_damage()
            enemy_target = random.randrange(0, len(players))
            players[enemy_target].hp -= enemy_damage
            print(BColors.RED + enemy.name + " attacked " + players[enemy_target].name + " for",
                  enemy_damage, "points." + BColors.END)

