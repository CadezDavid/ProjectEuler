import fractions

def koren_iz_dve(n):
    'Vrne n-ti približek v obliki ulomka in število prbližkov do n-tega, katerih števec ima več števk od imenovalca.'
    if n == 1:
        return 1
    else:
        stevec = 0
        priblizek = fractions.Fraction(1/2)
        for _ in range(1, n + 1):
            priblizek += fractions.Fraction(2)
            priblizek = fractions.Fraction(1) / fractions.Fraction(priblizek)
            if len(str(fractions.Fraction(priblizek + 1).numerator)) > len(str(fractions.Fraction(priblizek + 1).denominator)):
                stevec += 1
        return fractions.Fraction(priblizek + 1), stevec