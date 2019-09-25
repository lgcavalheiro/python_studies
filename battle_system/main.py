from classes.game import Person
from classes.game import BColors
from classes.healing_spell import HealingSpell
from classes.spell import Spell

fire = Spell("Fire", 10, 80)
ice = Spell("Ice", 5, 40)
ball_lightning = Spell("Ball Lightning", 20, 120)
heal = HealingSpell("Heal", 25, 50)

player = Person(hp=460, mp=100, atk=50, dfn=50, mag=[fire, ice, heal, ball_lightning])
foe = Person(hp=500, mp=80, atk=75, dfn=30, mag=[])

running = True
print(BColors.FAIL + BColors.BOLD + "A FOE ATTACKS!" + BColors.ENDC)

while running:
    print("-------------------------------------")  # BEGIN BATTLE
    player.choose_action()
    act = input("Choose an action:")  # PLAYER PICKS ACTION
    index = int(act) - 1

    if index == 0:  # ATTACK ACTION
        dmg = player.generate_dmg()
        foe.take_dmg(dmg=dmg)
        print("Player attacks for", BColors.FAIL, BColors.BOLD, dmg, "damage!", BColors.ENDC)
        print("Foe hp is: ", BColors.OKGREEN, foe.get_hp(), "/", foe.get_maxhp(), BColors.ENDC)
        print("Foe mp is: ", BColors.OKBLUE, foe.get_mp(), "/", foe.get_maxmp(), BColors.ENDC)
    elif index == 1:  # SPELL ACTION
        player.choose_magic()
        magic_choice = int(input("Choose spell: "))

        if magic_choice > len(player.mag) or magic_choice < 0:
            print(BColors.FAIL, BColors.BOLD, "Invalid spell index!", BColors.ENDC)
            continue

        spell = player.mag[magic_choice].get_spell_name()  # CHECK IF SPELL INDEX IS VALID

        cost = player.mag[magic_choice].get_spell_cost()
        curr_mp = player.get_mp()

        if cost > curr_mp:  # IF NOT ENOUGH MP
            print(BColors.FAIL + "You don't have enough Mana!" + BColors.ENDC)
            continue
        else:  # SUCCESSFUL SPELL CAST
            player.mag[magic_choice].cast_spell(caster=player, target=foe)
            print("Foe hp is: ", BColors.OKGREEN, foe.get_hp(), "/", foe.get_maxhp(), BColors.ENDC)
            print("Foe mp is: ", BColors.OKBLUE, foe.get_mp(), "/", foe.get_maxmp(), BColors.ENDC)
    else:  # IF ACTION IS INVALID
        print(BColors.FAIL, BColors.BOLD, "Invalid action!", BColors.ENDC)
        continue

    if foe.get_hp() <= 0:  # CHECK IF FOE IS DEAD
        print(BColors.OKBLUE + "Foe has died!" + BColors.ENDC)
        running = False
        break

    foedmg = foe.generate_dmg()  # FOE ATTACKS
    player.take_dmg(foedmg)
    print("Foe attacks for", BColors.FAIL, BColors.BOLD, foedmg, "damage!", BColors.ENDC)
    print("Player hp is: ", BColors.OKGREEN, player.get_hp(), "/", player.get_maxhp(), BColors.ENDC)
    print("Player mp is: ", BColors.OKBLUE, player.get_mp(), "/", player.get_maxmp(), BColors.ENDC)

    if player.get_hp() <= 0:  # CHECK IF PLAYER IS DEAD
        print(BColors.FAIL + "Player died!" + BColors.ENDC)
        running = False
        break
