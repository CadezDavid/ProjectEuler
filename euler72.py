import fractions
import math

# def phi(a):
#     b=a-1
#     c=0
#     while b:
#         if not fractions.gcd(a,b)-1:
#             c+=1
#         b-=1
#     return c

def stevilotujih(n):
    return len([i for i in range(1,n) if fractions.gcd(i,n) == 1])

def funkcija(n):
    if n == 1:
        return 0
    else:
        return stevilotujih(n) + funkcija(n-1)

def pradelitelji(n):
    list = []
    i = 2
    while i <= n:
        if n % i == 0:
            n //= i
            list.append(i)
        else:
            i += 1
    return set(list)

def phi2(n):
    produkt = n
    for i in pradelitelji(n):
        produkt *= 1 - 1 / i
    return int(produkt)

def vsota(n):
    sum = 0
    i = 2
    while i <= n:
        sum += phi(i)
        i += 1
    return sum

# def phi3(i):
#     return len({fractions.Fraction(m, n) for m in range(1, i+1) for n in range(1, i+1) if m < n})

def faktorialno(n):
    return math.factorial(n)

def primes2(n):
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

def factors(n):
    def prime_powers(n):
        n = int(n)
        for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
            if c*c > n:
                break
            if n % c:
                continue
            d,p = (), c
            while not n % c:
                n, p, d = n // c, p * c, d + (p,)
            yield(d)
        if n > 1: yield((n,))

    r = [1]
    for e in prime_powers(n):
        r += [ a * b for a in r for b in e]
    r.remove(1)
    if int(n) in r:
        r.remove(int(n))
    return r

def is_prime(n):
    n = int(n)
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

def samo_prastevilski_del(n):
    return [i for i in n if is_prime(i)]

# def phi4(n):
#     phi = n
#     list = samo_prastevilski_del(factors(n))
#     for i in list:
#         phi *= ( 1 - 1 / int(i) )
#     return phi

def rezultat(n):
    sum = 0
    for i in range(1, int(n)+1):
        sum += phi(i)
    return sum

import math
import fractions

def pradelitelji(n):
    list = []
    i = 2
    while i <= n:
        if n % i == 0:
            n //= i
            list.append(i)
        else:
            i += 1
    return set(list)

def is_prime(n):
    n = int(n)
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

def phi(n):
    produkt = n
    for i in pradelitelji(n):
        produkt *= 1 - 1 / i
    return int(produkt)

def maksimum(n):
    s = 0
    i = 1
    while i <= n:
        if is_prime(i) or i % 2 != 0 or i % 3 != 0 or i % 5 != 0 or i % 7 != 0 or i % 11 != 0 or i % 13 != 0:
            i += 1
        else:
            k = i / phi(i)
            s = max(s, k)
            if k == s:
                list = [i]
                i += 2
            else:
                i += 2
    return list