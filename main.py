import random
from Classes.Foe import Foe

foe1 = Foe(atkl=random.randrange(1, 49), atkh=random.randrange(50, 100),
           hp=random.randrange(100,200), mp=random.randrange(50,100))
foe1.getAtk()
foe1.getHpMp()

playerhp = 260
foeatkl = 10
foeatkh = 80
count = 0

while playerhp >= 0:
    dmg = random.randrange(foeatkl, foeatkh)
    count = count + 1
    playerhp = playerhp - dmg
    print("Foe attacked for: ", dmg, "Current hp is: ", playerhp)

    if playerhp > 30:
        continue

    if playerhp < 30:
        playerhp = 30
        print("Teleported to nearest inn")
        break
