import math

n = input("Do kod naj jih sešteje: ")

def pravi_delitelji(n):
    n = int(n)
    mnozica = {1}
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            mnozica.add(x)
            mnozica.add(n//x)
    return mnozica

def vsotadeliteljev(k):
    return sum(pravi_delitelji(k))

vsota_amicable_stevil = 0

for stevilo in range(1, int(n) + 1):
    if stevilo == vsotadeliteljev(vsotadeliteljev(stevilo)) and \
    stevilo != vsotadeliteljev(stevilo):
        vsota_amicable_stevil += stevilo

print(vsota_amicable_stevil)