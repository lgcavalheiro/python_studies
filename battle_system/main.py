from classes import color
from classes.game import Person
from classes.spell import Spell, HealingSpell
from classes.inventory import HealingItem, AttackItem
import random

fire = Spell("Fire", 10, 80)
ice = Spell("Ice", 5, 40)
ball_lightning = Spell("Ball Lightning", 20, 120)
heal = HealingSpell("Heal", 25, 50)

potion = HealingItem("Potion", "potion", "Heals for 50 HP", 50, "self")
high_potion = HealingItem("High Potion", "potion", "Heals for 100 HP", 100, "target")
super_potion = HealingItem("Super Potion", "potion", "Heals for 500 HP", 500, "all")
elixir = HealingItem("Elixir", "elixir", "Fully restores HP and MP", 9999, "self")
mega_elixir = HealingItem("Mega Elixir", "elixir", "Fully restores HP and MP for whole party", 9999, "all")
grenade = AttackItem("Grenade", "attack", "Deals 200 damage", 200, "target")

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

foe = Person(hp=500, mp=80, atk=45, dfn=30, mag=[], items=player_items, name="Gato com raiva")
foe2 = Person(hp=380, mp=200, atk=35, dfn=30, mag=[fire, ice, ball_lightning], items=[], name="Pai de santo")
foe3 = Person(hp=620, mp=30, atk=65, dfn=30, mag=[], items=[], name="Cigarrão Pedófilo")
foe4 = Person(hp=400, mp=30, atk=45, dfn=30, mag=[fire, ice], items=player_items, name="ET Bilú")
foeparty = [foe, foe2, foe3, foe4]

running = True
print(color.BColors.RED + color.BColors.BOLD + "A FOE ATTACKS!" + color.BColors.END)

while running:  # BEGIN BATTLE
    print("-------------------------------------")  # PRINT STATS FOR PARTY AND FOEPARTY
    for player in party:
        player.get_stats(party)
    print()

    for player in foeparty:
        player.get_stats(foeparty)
    print()

    for player in party:  # PARTY TURN
        if player.hp == 0:  # IF PLAYER IS DEAD SKIP TURN
            continue

        print("It's ", player.name, " turn!")
        player.choose_action()
        act = input("Choose an action:")  # PLAYER PICKS ACTION
        index = int(act) - 1

        if index == 0:  # ATTACK ACTION
            target = player.choose_target(foeparty=foeparty)  # CHOOSE TARGET
            if target < 0:  # CHECK IF TARGET IS VALID
                continue
            dmg = player.generate_dmg()  # PROCESS DAMAGE
            foeparty[target].take_dmg(dmg=dmg)
            print(player.get_name(), "attacks", foeparty[target].get_name()
                  , "for", color.BColors.RED + color.BColors.BOLD, dmg, "damage!", color.BColors.END)
            if foeparty[target].hp == 0:  # CHECK IF  TARGET DIED
                print(foeparty[target].name, "has"
                      , color.BColors.RED, color.BColors.BOLD, "FALLEN", color.BColors.END, "!")
                del foeparty[target]
            else:
                foeparty[target].get_stats(foeparty)
        elif index == 1:  # SPELL ACTION
            player.choose_magic()  # SPELL CHOICE
            magic_choice = int(input("Choose spell: ")) - 1
            if magic_choice == -1:  # CHECK IF BACK
                continue
            if magic_choice > len(player.mag) or magic_choice < 0:  # CHECK IF SPELL INDEX IS VALID
                print(color.BColors.RED, color.BColors.BOLD, "Invalid spell index!", color.BColors.END)
                continue
            spell = player.mag[magic_choice].get_spell_name()  # GET SPELL VARS
            cost = player.mag[magic_choice].get_spell_cost()
            curr_mp = player.get_mp()
            if cost > curr_mp:  # IF NOT ENOUGH MP
                print(color.BColors.RED + "You don't have enough Mana!" + color.BColors.END)
                continue
            else:  # SUCCESSFUL SPELL CAST
                target_index = player.choose_spell_target(foeparty=foeparty, magic=player.mag[magic_choice]
                                                          , party=party)  # CHOOSE TARGET FOR SPELL
                if type(player.mag[magic_choice]) is Spell:  # CHECK IF SPELL IS NORMAL SPELL
                    player.mag[magic_choice].cast_spell(caster=player, target=foeparty[target_index])
                    if foeparty[target_index].hp == 0:  # CHECK IF TARGET IS DEAD
                        print(foeparty[target_index].name, "has"
                              , color.BColors.RED, color.BColors.BOLD, "FALLEN", color.BColors.END, "!")
                        del foeparty[target_index]
                    else:
                        foeparty[target_index].get_stats(foeparty)
                elif type(player.mag[magic_choice]) is HealingSpell:  # CHECK IF SPELL IS HEALING SPELL
                    player.mag[magic_choice].cast_spell(caster=player, target=party[target_index])
                    party[target_index].get_stats(foeparty)
        elif index == 2:  # USE ITEM ACTION
            player.choose_item()  # CHOOSE ITEM
            item_choice = int(input("Choose item:")) - 1
            if item_choice == -1:  # CHECK IF ITEM IS VALID
                continue
            item = player.items[item_choice]  # GET ITEM AND REDUCE QTD
            player.items[item_choice]["qtd"] -= 1
            if type(item["item"]) is HealingItem:  # CHECK IF HEALING ITEM
                if item["item"].prop == 9999:  # CHECK PROP FOR 9999
                    if item["item"].reach == "self":  # CHECK REACH SELF
                        player.set_hp(player.get_maxhp())
                        player.set_mp(player.get_maxmp())
                        print("Player heals for ", player.get_maxhp(), " HP!")
                        print("Player heals for ", player.get_maxmp(), " MP!")
                    elif item["item"].reach == "all":  # CHECK REACH ALL
                        for ally in party:
                            ally.set_hp(player.get_maxhp())
                            ally.set_mp(player.get_maxmp())
                            print("Player heals for ", ally.get_maxhp(), " HP!")
                            print("Player heals for ", ally.get_maxmp(), " MP!")
                else:  # IF NORMAL PROP VALUE
                    if item["item"].reach == "self":  # CHECK REACH SELF
                        player.take_dmg(-item["item"].prop)
                        print("Player heals for ", item["item"].prop, " HP!")
                    elif item["item"].reach == "all":  # CHECK REACH ALL
                        for ally in party:
                            ally.take_dmg(-item["item"].prop)
                            print("Player heals for ", item["item"].prop, " HP!")
            elif item["item"].type == "attack":  # CHECK IF ATTACK ITEM
                foeparty[0].take_dmg(item["item"].prop)
                print("Foe takes ", item["item"].prop, " points of damage!")
                foeparty[0].get_stats(foeparty)
        else:  # IF ACTION IS INVALID
            print(color.BColors.RED, color.BColors.BOLD, "Invalid action!", color.BColors.END)
            continue

        if len(foeparty) == 0:  # CHECK IF FOEPARTY IS DEAD
            print(color.BColors.BLUE + "A winner is you!" + color.BColors.END)
            running = False
            break

    for currfoe in foeparty:  # FOE TURN
        foe_choice = random.randrange(0, len(currfoe.actions))
        if currfoe.actions[foe_choice] == "Attack":  # ATTACK CHOICE
            foedmg = currfoe.generate_dmg()  # FOE ATTACKS
            target_index = random.randrange(0, len(party))
            while party[target_index].hp == 0:  # CHECK IF PLAYER IS DEAD AND RE-CHOOSE IN CASE IT IS
                target_index = random.randrange(0, len(party))
                if party[target_index].hp > 0:
                    break
            party[target_index].take_dmg(foedmg)
            print(color.BColors.RED, currfoe.name, color.BColors.END
                  , "attacks", color.BColors.GREEN, party[target_index].name, color.BColors.END
                  , "for", color.BColors.RED, color.BColors.BOLD, foedmg, "damage!"
                  , color.BColors.END)
            party[target_index].get_stats(party)

            if party[target_index].hp == 0:  # CHECK IF PLAYER IS DEAD
                print(party[target_index].name, "has", color.BColors.RED, "FALLEN", color.BColors.END, "!")

            death_count = 0
            for player in party:  # CHECK IF ALL PLAYERS ARE DEAD
                if player.hp == 0:
                    death_count += 1

            if death_count == len(party):  # IF ALL PLAYERS DEAD
                print(color.BColors.RED + "A loser is you!" + color.BColors.END)
                running = False
                break
        elif currfoe.actions[foe_choice] == "Magic":  # SPELL CHOICE
            foe_spell = random.randrange(0, len(currfoe.mag))
            spell = currfoe.mag[foe_spell].get_spell_name()  # GET SPELL VARS
            cost = currfoe.mag[foe_spell].get_spell_cost()
            curr_mp = currfoe.get_mp()
            if cost > curr_mp:  # IF NOT ENOUGH MP
                print(color.BColors.RED + currfoe.name + "has failed to cast a spell!" + color.BColors.END)
                continue
            else:  # SUCCESSFUL SPELL CAST
                target_index = random.randrange(0, len(party))  # FOE TARGETS A PLAYER
                while party[target_index].hp == 0:  # CHECK IF PLAYER IS DEAD AND RE-CHOOSE IN CASE IT IS
                    target_index = random.randrange(0, len(party))
                    if party[target_index].hp > 0:
                        break
                currfoe.mag[foe_spell].cast_spell(caster=currfoe, target=party[target_index])
                party[target_index].get_stats(party)
                if party[target_index].hp == 0:  # CHECK IF PLAYER IS DEAD
                    print(party[target_index].name, "has", color.BColors.RED, "FALLEN", color.BColors.END, "!")

                death_count = 0
                for player in party:  # CHECK IF ALL PLAYERS ARE DEAD
                    if player.hp == 0:
                        death_count += 1

                if death_count == len(party):  # IF ALL PLAYERS DEAD
                    print(color.BColors.RED + "A loser is you!" + color.BColors.END)
                    running = False
                    break
        elif currfoe.actions[foe_choice] == "Use Items":  # ITEM CHOICE
            foe_item = random.randrange(0, len(currfoe.items))
            while currfoe.items[foe_item]["qtd"] == 0:
                foe_item = random.randrange(0, len(currfoe.items))
                if currfoe.items[foe_item]["qtd"] > 0:
                    break
            currfoe.items[foe_item]["qtd"] -= 1
            item = currfoe.items[foe_item]

            if type(item["item"]) is HealingItem:  # CHECK IF HEALING ITEM
                if item["item"].prop == 9999:  # CHECK PROP FOR 9999
                    if item["item"].reach == "self":  # CHECK REACH SELF
                        currfoe.set_hp(player.get_maxhp())
                        currfoe.set_mp(player.get_maxmp())
                        print(currfoe.name, "heals for ", currfoe.get_maxhp(), " HP!")
                        print(currfoe.name, "heals for ", currfoe.get_maxmp(), " MP!")
                    elif item["item"].reach == "all":  # CHECK REACH ALL
                        for ally in foeparty:
                            ally.set_hp(player.get_maxhp())
                            ally.set_mp(player.get_maxmp())
                            print(ally.name, "heals for ", ally.get_maxhp(), " HP!")
                            print(ally.name, "heals for ", ally.get_maxmp(), " MP!")
                else:  # IF NORMAL PROP VALUE
                    if item["item"].reach == "self":  # CHECK REACH SELF
                        currfoe.take_dmg(-item["item"].prop)
                        print(currfoe.name, "heals for ", item["item"].prop, " HP!")
                    elif item["item"].reach == "all":  # CHECK REACH ALL
                        for ally in foeparty:
                            ally.take_dmg(-item["item"].prop)
                            print(ally.name, "heals for ", item["item"].prop, " HP!")
            elif type(item["item"]) is AttackItem:  # CHECK IF ATTACK ITEM
                target_index = random.randrange(0, len(party))  # FOE TARGETS A PLAYER
                while party[target_index].hp == 0:  # CHECK IF PLAYER IS DEAD AND RE-CHOOSE IN CASE IT IS
                    target_index = random.randrange(0, len(party))
                    if party[target_index].hp > 0:
                        break
                party[target_index].take_dmg(item["item"].prop)
                print(currfoe.name, "uses", item["item"].name, "on", party[target_index].name
                      , "dealing", item["item"].prop, "points of damage!")
                party[target_index].get_stats(party)

                if party[target_index].hp == 0:  # CHECK IF PLAYER IS DEAD
                    print(party[target_index].name, "has", color.BColors.RED, "FALLEN", color.BColors.END, "!")

                death_count = 0
                for player in party:  # CHECK IF ALL PLAYERS ARE DEAD
                    if player.hp == 0:
                        death_count += 1

                if death_count == len(party):  # IF ALL PLAYERS DEAD
                    print(color.BColors.RED + "A loser is you!" + color.BColors.END)
                    running = False
                    break
