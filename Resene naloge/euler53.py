binomski_slovar = {(1, 1): 1}

for n in range(2, 101):
    for r in range(n + 1):
        if r == 0:
            binomski_slovar[(n, r)] = 1
        elif r == 1:
            binomski_slovar[(n, r)] = n
        elif r == n:
            binomski_slovar[(n, r)] = binomski_slovar[(n - 1, r - 1)] 
        else:
            binomski_slovar[(n, r)] = binomski_slovar[(n - 1, r)] + binomski_slovar[(n - 1, r - 1)]

stevilo_vecjih_od_milijon = sum( map( lambda x: x > 10 ** 6, binomski_slovar.values() ) )