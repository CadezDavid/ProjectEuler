matrika = list()
for i in list(open('euler82.txt', 'r')):
    matrika.append(i.replace('\n', '').split(','))

najboljsa_pot = dict()
for vrstica in range(80):
    najboljsa_pot[(0, vrstica)] = int(matrika[vrstica][0])

for stolpec in range(1, 80):
    for vrstica in range(80):
        najboljsa_pot[(stolpec, vrstica)] = min([
            najboljsa_pot[(stolpec - 1, zamik)] + sum([int(matrika[i][stolpec]) for i in range(min(vrstica, zamik), max(vrstica, zamik) + 1)]) for zamik in range(80)
        ])

najkrajsa_pot = min([
    najboljsa_pot[clen] for clen in najboljsa_pot.keys() if clen[0] == 79
])