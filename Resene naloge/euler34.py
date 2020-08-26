import math

skupna_vsota = 0

for stevilka in range(10, 10 ** 5):
    vsota = 0
    for stevka in str(stevilka):
        vsota += math.factorial(int(stevka))
    if vsota == stevilka:
        skupna_vsota += stevilka