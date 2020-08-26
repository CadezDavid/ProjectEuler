import math

n = int(input('Vpisi stevilko:'))

def vsota_stevk_v_fakulteti(n):
    n_fakulteta = str(math.factorial(n))
    stevec = 0
    for stevka in n_fakulteta:
        stevec += int(stevka)
    return stevec

print(vsota_stevk_v_fakulteti(n))