def je_prastevilo(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def poljuben_krog(n):
    return ( 2 * n - 1 ) ** 2 - ( 2 * ( n - 1 ) - 1 ) ** 2 if n != 1 else 1

def je_lih_kvadrat(n):
    return n ** ( 1 / 2 ) % 2 == 1

def seznam_krogov(n):
    seznam = list()
    s = 1
    trenutni = list()
    while len(seznam) != n:
        if je_lih_kvadrat(s):
            trenutni.append(s)
            seznam.append(trenutni)
            trenutni = list()
            s += 1
        else:
            trenutni.append(s)
            s += 1
    return seznam

def funkcija(n):
    seznam = [1]
    for i in range(2, n + 1):
        k = ( 2 * i - 1 ) ** 2
        p = k ** (1/2) - 1
        seznam += sorted([ int( k - i * p ) for i in range(1, 4)])
    return seznam

def delez(n):
    return len([i for i in funkcija(n) if je_prastevilo(i)]) / ( (n-1) * 4 + 1 )

slovar = {2: 0.6}
s = 0.6
n = 3

while s > 0.1:
    if n in slovar:
        s = slovar[n]
        n += 1
    else:
        p = 2 * n - 2
        t = [i for i in [int((2*n-1)**2 - i * p ) for i in range(1, 4)] if je_prastevilo(i)]
        s = (slovar[n-1] * ((n-2)*4+1) + len(t) ) / ( ( n - 1 ) * 4 + 1 )
        slovar[n] = s
        n += 1
