import random


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


class Person:
    def __init__(self, hp, mp, atk, dfn, mag):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.dfn = dfn
        self.mag = mag
        self.actions = ["Attack", "Magic"]

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

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        index = 1
        print("Actions: ")
        for item in self.actions:
            print(str(index) + ": " + item)
            index += 1

    def choose_magic(self):
        index = 0
        print("Spells: ")
        for _ in self.mag:
            print(str(index), ":", self.mag[index].get_spell_name(), " Cost: ", self.mag[index].get_spell_cost(),
                  "Magnitude: ", self.mag[index].get_spell_dmg())
            index += 1
