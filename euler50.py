def je_prastevilo(n):
    if n % 2 == 0:
        return n == 2
    else:
        i = 3
        while i ** 2 <= n:
            if n % i == 0:
                return False
            i += 2
    return True


sez = list()
for i in range(1, 10**6):
    if je_prastevilo(i):
        sez.append(i)

koncen = dict()

for i in range(1, 10000):
    for j in range(i+1, 10000):
        if sum(sez[i:j]) > 10**6:
            break
        if je_prastevilo(sum(sez[i:j])):
            koncen[j-i] = sum(sez[i:j])