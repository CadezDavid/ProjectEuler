import math

def trikotnisko(stevilo):
    return stevilo * (stevilo + 1) // 2

def je_pentagonalno(stevilo):
    return math.sqrt(1 + 24 * stevilo) % 6 == 5 and \
        float(round(math.sqrt(1 + 24 * stevilo))) == math.sqrt(1 + 24 * stevilo)

def je_heksagonalno(stevilo):
    return float(math.floor(math.sqrt(1 + 8 * stevilo))) == math.sqrt(1 + 8 * stevilo) and \
        int(math.sqrt(1 + 8 * stevilo)) % 4 == 3

kandidat = 286

while True:
    if je_heksagonalno(trikotnisko(kandidat)) and je_pentagonalno(trikotnisko(kandidat)):
        break
    kandidat += 1