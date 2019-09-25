import random

playerhp = 260
foeatkl = 10
foeatkh = 80
count = 0

while playerhp >= 0:
    dmg = random.randrange(foeatkl, foeatkh)
    count = count + 1
    playerhp = playerhp - dmg
    if playerhp < 30:
        playerhp = 30
        print("Teleported to nearest inn")
        break

    print("Foe attacked for: ", dmg, "Current hp is: ", playerhp)