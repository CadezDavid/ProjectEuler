import math

def vsota_stevk(n):
    vsota = 0
    for i in n:
        vsota += int(i)
    return vsota

def je_prastevilo(stevilo):
    for i in range(2, int(math.sqrt(stevilo)) + 1):
        if stevilo % i == 0:
            return False
    return True

indeks = 1
kandidat = 3

while indeks < 10001:
    if je_prastevilo(kandidat):
        zadnje_prastevilo = kandidat
        indeks += 1
    kandidat += 2

print(zadnje_prastevilo)