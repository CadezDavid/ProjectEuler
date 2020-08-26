import math

def je_pentagonalno(stevilo):
    return math.sqrt( 1 + 24 * stevilo ) % 6 == 5 and float(round(math.sqrt( 1 + 24 * stevilo ))) == math.sqrt( 1 + 24 * stevilo )

def pentagonalno(stevilo):
    return stevilo * ( 3 * stevilo - 1 ) // 2

i = 5
D = 0

while D == 0:
    for k in range(1, i):
        a = pentagonalno(i)
        b = pentagonalno(k)
        if je_pentagonalno( a - b ) and je_pentagonalno( a + b ):
            D = a - b
    i += 1