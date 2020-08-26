def je_pandigital(n):
    for i in range(1, 10):
        if not str(i) in str(n):
            return False
    return len(str(n)) == 9

def concaten(stevilo):
    vsota = ''
    stevec = 1
    while len(vsota) < 9:
        vsota += str(stevec * int(stevilo))
        stevec += 1
    return je_pandigital(vsota), vsota

seznam = list()

for stevilo in range(1, 10 ** 5):
    if concaten(stevilo)[0]:
        seznam.append(concaten(stevilo)[1])

print(seznam, '\n', max(seznam))