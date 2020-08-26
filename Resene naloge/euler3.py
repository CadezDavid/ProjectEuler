import math

def prastevilski_delitelji(stevilo):
    i = 2
    mnozica = set()
    while i <= stevilo:
        if stevilo % i == 0:
            mnozica.add(i)
            while stevilo % i == 0:
                stevilo //= i
        i += 1
    return mnozica

def najvecji_prastevilski_delitelj(stevilo):
    return max(prastevilski_delitelji(stevilo))

print(najvecji_prastevilski_delitelj(600851475143))