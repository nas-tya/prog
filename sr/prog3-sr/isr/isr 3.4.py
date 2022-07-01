def crypto(string, delt=13):
    UA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LA = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in string:
        if (i.islower()):
            res += LA[(LA.index(i) + delt) % len(LA)]
        else:
            res += UA[(UA.index(i) + delt) % len(UA)]
    return res
print(crypto('exxegoexsrgi'))