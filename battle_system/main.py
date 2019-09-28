from classes.game import Person
from classes.game import BColors
from classes.healing_spell import HealingSpell
from classes.spell import Spell
from classes.inventory import Item
import random

fire = Spell("Fire", 10, 80)
ice = Spell("Ice", 5, 40)
ball_lightning = Spell("Ball Lightning", 20, 120)
heal = HealingSpell("Heal", 25, 50)

potion = Item("Potion", "potion", "Heals for 50 HP", 50)
high_potion = Item("High Potion", "potion", "Heals for 100 HP", 100)
super_potion = Item("Super Potion", "potion", "Heals for 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP and MP", 9999)
mega_elixir = Item("Mega Elixir", "elixir", "Fully restores HP and MP for whole party", 9999)
grenade = Item("Grenade", "attack", "Deals 200 damage", 200)

player_magic = [fire, ice, heal, ball_lightning]
player_items = [{"item": potion, "qtd": 5}
    , {"item": high_potion, "qtd": 3}
    , {"item": super_potion, "qtd": 1}
    , {"item": elixir, "qtd": 3}
    , {"item": mega_elixir, "qtd": 2}
    , {"item": grenade, "qtd": 8}]

player = Person(hp=360, mp=150, atk=50, dfn=50, mag=player_magic, items=player_items, name="Juberto")
player2 = Person(hp=460, mp=50, atk=50, dfn=50, mag=player_magic, items=player_items, name="Cacimbinha")
player3 = Person(hp=400, mp=100, atk=50, dfn=50, mag=player_magic, items=player_items, name="Baianinho da Sinuca")
party = [player, player2, player3]

foe = Person(hp=500, mp=80, atk=75, dfn=30, mag=[], items=[], name="Goblin")
foe2 = Person(hp=3800, mp=200, atk=35, dfn=30, mag=[fire, ice, ball_lightning], items=[], name="Warlock")
foe3 = Person(hp=620, mp=30, atk=105, dfn=30, mag=[], items=[], name="Ogre")
foeparty = [foe, foe2, foe3]

running = True
print(BColors.RED + BColors.BOLD + "A FOE ATTACKS!" + BColors.END)

while running:
    print("-------------------------------------")  # BEGIN BATTLE
    for player in party:
        player.get_stats(party)
    print()

    for player in foeparty:
        player.get_stats(foeparty)
    print()

    for player in party:
        print("It's ", player.name, " turn!")
        player.choose_action()
        act = input("Choose an action:")  # PLAYER PICKS ACTION
        index = int(act) - 1

        if index == 0:  # ATTACK ACTION
            target = player.choose_target(foeparty=foeparty)
            if target < 0:
                continue
            dmg = player.generate_dmg()
            foeparty[target].take_dmg(dmg=dmg)
            print(player.get_name(), "attacks", foeparty[target].get_name()
                  , "for", BColors.RED + BColors.BOLD, dmg, "damage!", BColors.END)
            foeparty[target].get_stats(foeparty)
        elif index == 1:  # SPELL ACTION
            player.choose_magic()
            magic_choice = int(input("Choose spell: ")) - 1
            if magic_choice == -1:
                continue
            if magic_choice > len(player.mag) or magic_choice < 0:  # CHECK IF SPELL INDEX IS VALID
                print(BColors.RED, BColors.BOLD, "Invalid spell index!", BColors.END)
                continue
            spell = player.mag[magic_choice].get_spell_name()
            cost = player.mag[magic_choice].get_spell_cost()
            curr_mp = player.get_mp()
            if cost > curr_mp:  # IF NOT ENOUGH MP
                print(BColors.RED + "You don't have enough Mana!" + BColors.END)
                continue
            else:  # SUCCESSFUL SPELL CAST
                target_index = player.choose_spell_target(foeparty=foeparty, magic=player.mag[magic_choice], party=party)
                player.mag[magic_choice].cast_spell(caster=player, target=foeparty[target_index])
                foeparty[target_index].get_stats(foeparty)
        elif index == 2:  # USE ITEM ACTION
            player.choose_item()
            item_choice = int(input("Choose item:")) - 1
            if item_choice == -1:
                continue
            item = player.items[item_choice]
            player.items[item_choice]["qtd"] -= 1
            if item["item"].type == "potion":
                player.take_dmg(-item["item"].prop)
                print("Player heals for ", item["item"].prop, " HP!")
            elif item["item"].type == "elixir":
                player.set_hp(player.get_maxhp())
                player.set_mp(player.get_maxmp())
                print("Player heals for ", player.get_maxhp(), " HP!")
                print("Player heals for ", player.get_maxmp(), " MP!")
            elif item["item"].type == "attack":
                foeparty[0].take_dmg(item["item"].prop)
                print("Foe takes ", item["item"].prop, " points of damage!")
                foeparty[0].get_stats(foeparty)
        else:  # IF ACTION IS INVALID
            print(BColors.RED, BColors.BOLD, "Invalid action!", BColors.END)
            continue

        if foeparty[0].get_hp() <= 0:  # CHECK IF FOE IS DEAD
            print(BColors.BLUE + "Foe has died!" + BColors.END)
            running = False
            break

    for currfoe in foeparty:
        foedmg = currfoe.generate_dmg()  # FOE ATTACKS
        target_index = random.randrange(0, len(party))
        party[target_index].take_dmg(foedmg)
        print("Foe attacks for", BColors.RED, BColors.BOLD, foedmg, "damage!", BColors.END)
        party[target_index].get_stats(party)

        if player.get_hp() <= 0:  # CHECK IF PLAYER IS DEAD
            print(BColors.RED + "Player died!" + BColors.END)
            running = False
            break
