import random

from classes import color


class Spell:
    def __init__(self, name, cost, dmg):
        self.name = name
        self.cost = cost
        self.dmg = dmg

    def generate_spell_dmg(self):
        mgl = self.dmg - 5
        mgh = self.dmg + 5
        return random.randrange(mgl, mgh)

    def get_spell_name(self):
        return self.name

    def get_spell_cost(self):
        return self.cost

    def get_spell_dmg(self):
        return self.dmg

    def cast_spell(self, caster, target):
        caster.reduce_mp(self.cost)
        dmg = self.generate_spell_dmg()
        target.take_dmg(dmg)
        print(color.BColors.BLUE, caster.get_name()
              , color.BColors.END, "casts"
              , color.BColors.RED, self.name
              , color.BColors.END, "on"
              , color.BColors.RED, target.get_name()
              , color.BColors.END, "dealing"
              , color.BColors.RED, dmg
              , color.BColors.END, "points of damage!")


class HealingSpell(Spell):
    def generate_spell_dmg(self):
        return -self.dmg

    def cast_spell(self, caster, target):
        caster.reduce_mp(self.cost)
        dmg = self.generate_spell_dmg()
        target.take_dmg(dmg)
        print(color.BColors.BLUE, caster.get_name()
              , color.BColors.END, "casts"
              , color.BColors.GREEN, self.name
              , color.BColors.END, "on"
              , color.BColors.GREEN, target.get_name()
              , color.BColors.END, "healing for"
              , color.BColors.GREEN, -dmg
              , color.BColors.END, "health points!")
