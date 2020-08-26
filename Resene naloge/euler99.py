def primerjaj_par(stevilo0, stevilo1):
    '''Stevili sta lista dolzine 2, kjer je prvi element osnova in drugi eksponent.'''
    if int(stevilo0[0]) ** (int(stevilo0[1]) / int(stevilo1[1])) < int(stevilo1[0]):
        return 1
    return 0

with open('euler99.txt', 'r') as document:
    document = list(document)
    najvecji = document[0].strip().split(',')
    indeks = 0
    for stevilo, i in zip(document, range(len(document))):
        if primerjaj_par(najvecji, stevilo.strip().split(',')) == 1:
            najvecji = stevilo.strip().split(',')
            indeks = i