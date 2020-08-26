neurejena_piramida = list(open('euler18.txt', 'r'))

piramida = list()

for vrstica in neurejena_piramida:
    vrstica = [int(stevilka) for stevilka in vrstica.rstrip().split(' ')]
    piramida.append(vrstica)

def pot(visina, sirina, resitve):
    if visina == sirina == 0:
        return int(piramida[visina][sirina])
    elif sirina == 0:
        return int(pot(visina - 1, sirina, resitve)) + int(piramida[visina][sirina])
    else:
        zg_levo = resitve.get((visina - 1, sirina), 0)
        zg_desno = resitve.get((visina - 1, sirina - 1), 0) 
        maksimalna_do_tja = max(zg_desno, zg_levo)
        return int(maksimalna_do_tja) + int(piramida[visina][sirina])

resitve = dict()

najvecja_vsota = 0

for i in range(len(piramida)):
    for j in range( i + 1 ):
        resitve[(i, j)] = pot(i, j, resitve)
        if i == 14:
            najvecja_vsota = max(najvecja_vsota, resitve[(i, j)])