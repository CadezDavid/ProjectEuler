stevilka = ''.join(list(map(str.strip, list(open('euler8.txt','r')))))
stevilke = stevilka.split('0')
stevilke = [stevilka for stevilka in stevilke if len(stevilka) > 12]

def produkt_niza(n):
    produkt = 1
    for i in n:
        produkt *= int(i)
    return produkt

def produkt_prvih_trinajst(n):
    return produkt_niza(n[:13])

najvecji_produkt = 0

for kandidat in stevilke:
    for začenši_z in range(len(kandidat) - 13 + 1):
        najvecji_produkt = max(najvecji_produkt, produkt_prvih_trinajst(kandidat[začenši_z:]))