#from classes.game import BColors
from classes.spell import Spell


class HealingSpell(Spell):
    def generate_spell_dmg(self):
        return -self.dmg

    def cast_spell(self, caster, target):
        target = caster
        caster.reduce_mp(self.cost)
        dmg = self.generate_spell_dmg()
        target.take_dmg(dmg)
        print("Player casts", self.name, "healing himself for", -dmg, "points of health!")
