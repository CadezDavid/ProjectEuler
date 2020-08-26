import itertools

stevke = ['1', '3', '7', '9']

def je_prastevilo(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0 or n % 2 == 0:
            return False
        i += 2
    return True

def zasukej(nabor):
    stevilo = list(nabor)
    seznam = []
    while len(seznam) < len(stevilo):
        seznam.append(int(''.join(stevilo)))
        stevilo.insert(0, stevilo.pop())
    return seznam

circular_primes = []

for ponavljanje in range(1, 7):
    for stevilo in itertools.product(stevke, repeat=ponavljanje):
        if all(je_prastevilo(permutacija) for permutacija in zasukej(stevilo)):
            circular_primes += zasukej(stevilo)

for stevilo in range(10):
    if je_prastevilo(stevilo):
        circular_primes.append(stevilo)

print(sorted(list(set(circular_primes))), len(set(circular_primes)))