import random

from classes import spell
from classes import healing_spell


class BColors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

    def disable(self):
        self.PINK = ''
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.END = ''


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
        self.actions = ["Attack", "Magic", "Use Items"]
        self.items = items
        self.name = name

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return "Current hp:", self.hp, "Max hp: ", self.maxhp

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
        print(BColors.GREEN + BColors.BOLD + "ACTIONS: " + BColors.END)
        for item in self.actions:
            print("    " + str(index) + ": " + item)
            index += 1

    def choose_magic(self):
        index = 1
        print("\n" + BColors.BLUE + BColors.BOLD + "SPELLS: " + BColors.END)
        for _ in self.mag:
            print("    " + str(index) + "." + self.mag[index - 1].get_spell_name() + " | Cost: "
                  + str(self.mag[index - 1].get_spell_cost())
                  + " | Magnitude: " + str(self.mag[index - 1].get_spell_dmg()))
            index += 1
        print("    " + "0 to go back")

    def choose_item(self):
        i = 1
        print("\n" + BColors.GREEN + BColors.BOLD + "ITEMS: " + BColors.END)
        for item in self.items:
            print("    " + str(i) + ". " + item["item"].name + " : " + item["item"].description + " x"
                  + str(item["qtd"]))
            i += 1
        print("    " + "0 to go back")

    def choose_target(self, foeparty):
        i = 0
        print("TARGETS:")
        for foe in foeparty:
            print(i + 1, ".", foe.get_name())
            i += 1
        print("0. to return")
        target = int(input("Choose a target: ")) - 1
        return target

    def choose_spell_target(self, foeparty, party, magic):
        if isinstance(magic, str):
            i = 0
            print("TARGETS:")
            for foe in foeparty:
                print(i + 1, ".", foe.get_name())
                i += 1
            print("0. to return")
            target = int(input("Choose a target: ")) - 1
            return target
        elif isinstance(magic, int):
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

        print(BColors.BOLD + self.name + name_space + " : "
              + "HP " + str(self.hp) + "/" + str(self.maxhp) + hp_space + " " + BColors.GREEN + hpbar
              + BColors.END + BColors.BOLD + "   "
              + "MP " + str(self.mp) + "/" + str(self.maxmp) + mp_space + BColors.BLUE + mpbar
              + BColors.END)
