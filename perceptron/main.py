def mu():
    output = 0
    for s in signals:
        print("S", s[0])
        print("W", s[1])
        output += int(s[0]) * int(s[1])
    return output


def activ():
    if mu_out >= limiar:
        return 1
    else:
        return 0


s1 = input("Define first signal:")
s2 = input("Define second signal:")
limiar = 1
w1 = 1
w2 = 1
d1 = [s1, w1]
d2 = [s2, w2]
signals = [d1, d2]

mu_out = mu()
print(mu_out)
print(activ())
