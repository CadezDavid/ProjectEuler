import math

zacetek = 1001005086220

def je_kvadrat(stevilo):
    return math.floor(math.sqrt(stevilo)) ** 2 == stevilo or \
        math.ceil(math.sqrt(stevilo)) ** 2 == stevilo

switch = True

while switch:
    if je_kvadrat(1 + 2 * zacetek * (zacetek + 1)) or \
        je_kvadrat(1 + 2 * zacetek * (zacetek - 1)):
        switch = False
        print(zacetek)
    zacetek += 4