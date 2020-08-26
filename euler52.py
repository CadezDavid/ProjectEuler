def imata_enake_stevke(n, m):
    return sorted(list(str(n))) == sorted(list(str(m)))

def veckratniki(n):
    for veckratnik in range(1, 7):
        if not imata_enake_stevke(n, n * veckratnik):
            return False
    return True

stevilo = 0
kandidat = 10

while stevilo == 0:
    if int(str(kandidat)[0:2]) > 16:
        pass
    else:
        if veckratniki(kandidat):
            stevilo = kandidat
    kandidat += 1