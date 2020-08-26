import fractions
import math

def modulus(n):
    if n % 3 == 0:
        return 2 * ( n // 3 )
    elif n == 1:
        return 2
    else:
        return 1

def priblizek(n, i=1):
    if i == n:
        return fractions.Fraction(modulus(i), 1)
    return fractions.Fraction(modulus(i) + fractions.Fraction(1, priblizek(n, i + 1)), 1)

def vsotastevca(n):
    return sum([int(i) for i in str(n.numerator)])