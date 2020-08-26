import math

def binomska_formula(a, b):
    return math.factorial(a) // ( math.factorial(b) * math.factorial( a - b ) )

print(binomska_formula(40, 20))