import math

list = []
i = 3

def je_prastevilo(n):
    if n < 2 or n == 4 or n == 6 or n == 8:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0 or n % 2 == 0:
            return False
        i += 2
    return True

def dvakrat_kvadrat(n):
    return math.floor((n/2)**(1/2)) == (n/2)**(1/2)

while len(list) == 0:
    if not je_prastevilo(i):
        sez = []
        for p in range(i):
            if je_prastevilo( i - p ) and dvakrat_kvadrat( p ):
                sez.append(i)
        if len(sez) == 0:
            list.append(i)
    i += 2