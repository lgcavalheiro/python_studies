import random

from classes import color
from classes.spell import Spell, HealingSpell


class Person:
    def __init__(self, name, hp, mp, atk, dfn, mag, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.dfn = dfn
        self.mag = mag
        self.actions = ["Attack"]
        if mag:
            self.actions.insert(len(self.actions),"Magic")
        if items:
            self.actions.insert(len(self.actions), "Use Items")
        self.items = items
        self.name = name

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def set_hp(self, hp):
        self.hp = hp

    def set_mp(self, mp):
        self.mp = mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_name(self):
        return self.name

    def choose_action(self):
        index = 1
        print(color.BColors.GREEN + color.BColors.BOLD + "ACTIONS: " + color.BColors.END)
        for item in self.actions:
            print("    " + str(index) + ": " + item)
            index += 1

    def choose_magic(self):
        index = 1
        print("\n" + color.BColors.BLUE + color.BColors.BOLD + "SPELLS: " + color.BColors.END)
        for _ in self.mag:
            print("    " + str(index) + "." + self.mag[index - 1].get_spell_name() + " | Cost: "
                  + str(self.mag[index - 1].get_spell_cost())
                  + " | Magnitude: " + str(self.mag[index - 1].get_spell_dmg()))
            index += 1
        print("    " + "0 to go back")

    def choose_item(self):
        i = 1
        print("\n" + color.BColors.GREEN + color.BColors.BOLD + "ITEMS: " + color.BColors.END)
        for item in self.items:
            print("    " + str(i) + ". " + item["item"].name + " : " + item["item"].description + " x"
                  + str(item["qtd"]))
            i += 1
        print("    " + "0 to go back")

    @staticmethod
    def choose_target(foeparty):
        i = 0
        print("TARGETS:")
        for foe in foeparty:
            print(i + 1, ".", foe.get_name())
            i += 1
        print("0. to return")
        target = int(input("Choose a target: ")) - 1
        return target

    @staticmethod
    def choose_spell_target(foeparty, party, magic):
        if type(magic) is Spell:
            i = 0
            print("TARGETS:")
            for foe in foeparty:
                print(i + 1, ".", foe.get_name())
                i += 1
            print("0. to return")
            target = int(input("Choose a target: ")) - 1
            return target
        elif type(magic) is HealingSpell:
            i = 0
            print("TARGETS:")
            for ally in party:
                print(i + 1, ".", ally.get_name())
                i += 1
            print("0. to return")
            target = int(input("Choose a target: ")) - 1
            return target

    def get_stats(self, party):
        hpbar = ""
        hpbar_ticks = (self.hp / self.maxhp) * 100 / 4
        mpbar = ""
        mpbar_ticks = (self.mp / self.maxmp) * 100 / 14

        while len(hpbar) < int(hpbar_ticks):
            hpbar += "▓"
        while len(hpbar) < 25:
            hpbar += " "

        while len(mpbar) < int(mpbar_ticks):
            mpbar += "▓"
        while len(mpbar) < 10:
            mpbar += " "

        index = 0
        name_length = []
        for member in party:
            name_length.insert(index, len(member.name))
            index += 1
        greater = max(name_length)

        name_space = ""
        while len(name_space) + len(self.name) < greater:
            name_space += " "

        hp_space = ""
        while len(str(self.hp) + "/" + str(self.maxhp)) + len(hp_space) < 9:
            hp_space += " "

        mp_space = ""
        while len(str(self.mp) + "/" + str(self.maxmp)) + len(mp_space) < 9:
            mp_space += " "

        print(color.BColors.BOLD + self.name + name_space + " : "
              + "HP " + str(self.hp) + "/" + str(self.maxhp) + hp_space + " " + color.BColors.GREEN + hpbar
              + color.BColors.END + color.BColors.BOLD + "   "
              + "MP " + str(self.mp) + "/" + str(self.maxmp) + mp_space + color.BColors.BLUE + mpbar
              + color.BColors.END)
