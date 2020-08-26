import math

rezultat = 1

for stevilo in range(1, 20):
    rezultat = stevilo * rezultat // math.gcd(stevilo, rezultat)

print(rezultat)