def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def dolzina_verige(n):
    if n != 1:
        return dolzina_verige(naslednji_clen(n)) + 1
    else:
        return 1

najdaljsi = 0
dolzina = 0

for stevilo in range(1, 10 ** 6):
    dolzina_trenutna = dolzina_verige(stevilo)
    if dolzina_trenutna > dolzina:
        najdaljsi = stevilo
        dolzina = dolzina_trenutna