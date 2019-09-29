import random


def try_sum(payload):
    tsum = 0.0
    sel = []

    for i in payload:
        tsum += i
        tsum = round(tsum, 2)
        sel.insert(len(sel), i)
        if tsum < 7.11:
            pass
        elif tsum > 7.11:
            return round(tsum - 7.11, 2)
        elif tsum == 7.11:
            print(tsum)
            return sel


def try_sel(payload, corr):
    if corr == 0:
        i = 0
        res_sel = []
        while i < 8:
            res_sel.insert(len(res_sel), payload[i])
            i += 1
        return res_sel
    elif corr < 0:
        for p in payload:
            pass
    elif corr > 0:
        pass


def taboo_bit(itera, goal, payload):
    i = 0
    tsum = 0
    while i < itera:
        j = 0
        bpayload = payload.copy()
        sel = []
        sel.clear()
        while j < len(bpayload):
            index = random.randrange(0, len(bpayload))
            sel.insert(len(sel), bpayload[index])
            bpayload.pop(index)
            j += 1
        for s in sel:
            tsum += s
        tsum = round(tsum, 2)
        if tsum == goal:
            return sel
        else:
            i += 1


nlist = [1.1, 1.2, 1.25, 1.41, 1.5, 1.63, 2.05, 2.22, 2.65, 2.9, 3.04, 3.16]
# testlist = [nlist[0], nlist[1], nlist[2], nlist[3], nlist[4]]
# trysum = try_sum(nlist)

nsel = taboo_bit(100, 7.11, nlist)

if nsel is not None:
    for n in nsel:
        print(n)
else:
    print("FAIL")
