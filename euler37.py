prve_stiri = [2, 3, 5, 7]

def je_prastevilo(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n > 1

def trunctable_z_desne(n):
    for indeks in range(1, len(str(n))):
        if not je_prastevilo(int(str(n)[0:indeks])):
            return False
    return n > 10

def trunctable_z_leve(n):
    for indeks in range(len(str(n))):
        if not je_prastevilo(int(str(n)[indeks:])):
            return False
    return n > 10

seznam = list()
vsota = 0

for stevilo in range(1, 10 ** 6):
    if trunctable_z_desne(stevilo) and trunctable_z_leve(stevilo):
        vsota += stevilo
        seznam.append(stevilo)