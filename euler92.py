import itertools

def kvadrati_stevk(n):
    produkt = 0
    for stevka in str(n):
        produkt += int(stevka) ** 2
    return produkt

def ali_pride_do_89(n):
    while not (n == 89 or n == 1):
        produkt = 0
        for stevka in str(n):
            produkt += int(stevka) ** 2
        n = produkt
    return n == 89

stevec = 0
for i in range(1, 10**7):
    if ali_pride_do_89(i):
        stevec += 1