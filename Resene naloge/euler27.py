import math

def je_prastevilo(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def polinom(n, a, b):
    return n ** 2 + a * n + b

prastevila = []
for i in range(1, 1000):
    if je_prastevilo(i):
        prastevila.append(i)
        prastevila.append(-i)

zaporednih_prastevil = 0

for a in prastevila:
    for b in prastevila:
        n = 0
        while je_prastevilo(polinom(n, a, b)):
            n += 1
        if n > zaporednih_prastevil:
            zaporednih_prastevil = n
            trenutna_favorita = (a, b)