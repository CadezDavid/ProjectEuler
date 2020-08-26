def stevilo_pravokotnikov(sirina, visina):
    vsota = 0
    for x in range(1, sirina + 1):
        for y in range(1, visina + 1):
            vsota += (sirina - x + 1) * (visina - y + 1)
    return vsota


najblizje = 2 * 10 ** 6

for a in range(100):
    for b in range(100):
        kandidat = abs(2 * 10 ** 6 - stevilo_pravokotnikov(a, b))
        if najblizje > kandidat:
            povrsina = (a * b, a, b)
            najblizje = kandidat