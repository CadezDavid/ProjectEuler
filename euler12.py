def nto_trikotnisko_st(n):
    return sum(range(n + 1))

def prafaktorji(stevilo):
    slovar_prafaktorjev = dict()
    prafaktor = 2
    while prafaktor <= stevilo:
        if stevilo % prafaktor == 0:
            potenca = 0
            while stevilo % prafaktor == 0:
                stevilo //= prafaktor
                potenca += 1
            slovar_prafaktorjev[prafaktor] = potenca
        prafaktor += 1
    return slovar_prafaktorjev

def produkt_seznama(seznam):
    produkt = 1
    for element in seznam:
        produkt *= element
    return produkt

def stevilo_deliteljev(stevilo):
    potence_prafaktorjev = prafaktorji(stevilo).values()
    mozne_kombinacije_potenc = [potenca + 1 for potenca in potence_prafaktorjev]
    return produkt_seznama(mozne_kombinacije_potenc)

kandidat = 0
delitelji = 0

while delitelji <= 500:
    kandidat += 1
    delitelji = stevilo_deliteljev(nto_trikotnisko_st(kandidat))