matrika = list()
for i in list(open('euler81.txt', 'r')):
    matrika.append(i.replace('\n', '').split(','))

def najboljsa_pot(vrstice, stolpci, resitve):
    if stolpci == 0:
        return sum([ int(matrika[i][0]) for i in range(vrstice + 1)])
    elif vrstice == 0:
        return sum([ int(matrika[0][j]) for j in range(stolpci + 1)])
    else:
        return int(matrika[vrstice][stolpci]) + min(resitve[(vrstice - 1, stolpci)], resitve[(vrstice, stolpci - 1)])

resitve = dict()
for i in range(80):
    for j in range(80):
        resitve[(i, j)] = najboljsa_pot(i, j, resitve)   