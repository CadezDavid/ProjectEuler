piramida = list(open('euler67.txt', 'r'))
piramida2 = list()
for i in piramida:
    piramida2.append(i.replace('\n', '').split(' '))

def pot(visina, sirina, resitve):
    if visina == sirina == 0:
        return int(piramida2[visina][sirina])
    elif sirina == 0:
        return int(pot(visina - 1, sirina, resitve)) + int(piramida2[visina][sirina])
    else:
        maksimalna_do_tja = max( int( resitve.get( (visina - 1, sirina), 0 ) ) , int( resitve.get( (visina - 1, sirina - 1), 0 ) ) )
        return int(maksimalna_do_tja) + int(piramida2[visina][sirina])

resitve = dict()

for i in range(len(piramida2)):
    for j in range(i+1):
        resitve[(i, j)] = pot(i, j, resitve)