import math

def pandigital(x):
    return len(str(x)) == len(set(str(x))) == int(max(set(str(x))))

def je_prastevilo(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

kandidat = 0
stevilo = 7654321

while kandidat == 0:
    if pandigital(stevilo) and je_prastevilo(stevilo):
        kandidat = stevilo
    stevilo -= 2