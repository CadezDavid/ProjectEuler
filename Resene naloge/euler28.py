def st_na_diagonali(n):
    seznam = [1]
    for obroc in range(2, n + 1):
        k = ( 2 * obroc - 1 ) ** 2
        p = k ** (1/2) - 1
        seznam += sorted([int( k - i * p ) for i in range(4)])
    return seznam

def vsota_st_na_diagonali(n):
    return sum(st_na_diagonali(n))