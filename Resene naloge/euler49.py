import itertools

def primes2(n):
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

kandidati = [i for i in primes2(10000) if len(str(i)) == 4]

akdgdsmgdsmg = list()

for i in kandidati:
    permutacije = list({int(''.join(k)) for k in itertools.permutations(str(i), 4) if int(''.join(k)) in kandidati})
    for m in sorted(permutacije)[:-1]:
        if 2 * sorted(permutacije)[sorted(permutacije).index(m)+1] - m in permutacije:
            akdgdsmgdsmg.append([m, sorted(permutacije)[sorted(permutacije).index(m)+1], 2 * sorted(permutacije)[sorted(permutacije).index(m)+1] - m])