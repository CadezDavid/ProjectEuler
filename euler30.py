def je_vsota_potenc_stevk(n):
    return n == sum([int(stevka) ** 5 for stevka in str(n)]) and len(str(n)) > 2

vsota = 0

for stevilo in range(10 ** 6):
    if je_vsota_potenc_stevk(stevilo):
        vsota += stevilo