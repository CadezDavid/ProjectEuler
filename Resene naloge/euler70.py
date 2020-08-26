import collections
import fractions
import math

def pradelitelji(n):
    delitelji = set()
    i = 3
    if n % 2 == 0:
        delitelji.add(2)
        n //= 2
    while i <= n:
        while n % i == 0:
            delitelji.add(i)
            n //= i
        i += 2
    return delitelji

def n_deljeno_s_fi_od_n(n):
    fi = 1
    for delitelj in pradelitelji(n):
        fi *= 1 - 1 / delitelj
    return 1 / fi

def phi(n):
    produkt = n
    for i in pradelitelji(n):
        produkt *=  1 - 1 / i 
    return int(produkt)


def je_prastevilo(n):
    if n < 2:
         return False
    if n % 2 == 0:
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def je_permutacija(n, m):
    return collections.Counter(str(m)) == collections.Counter(str(n))

najboljsi = 10
trenutni = 1


for i in range(2000, 5000):
    for k in range(i, 5000):
        if je_prastevilo(i) and je_prastevilo(k):
            if k * i > 10 ** 7:
                break
            if (i * k) / ((i - 1) * (k - 1)) < najboljsi and je_permutacija((i * k) , ((i - 1) * (k - 1))):
                najboljsi = (i * k) / ((i - 1) * (k - 1))
                trenutni = i * k