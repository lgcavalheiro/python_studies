class Foe:
    def __init__(self, atkl, atkh, hp, mp):
        self.atkl = atkl
        self.atkh = atkh
        self.hp = hp
        self.mp = mp

    def getAtk(self):
        print("atk low: ", self.atkl, "Atk High: ", self.atkh)

    def getHpMp(self):
        print("Hp is: ", self.hp, "Mp is: ", self.mp)