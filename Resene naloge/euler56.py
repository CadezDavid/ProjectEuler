def sestej_stevke(stevilo):
    return sum([int(stevka) for stevka in str(stevilo)])

najvecja = 0

for a in range(1, 101):
    for b in range(1, 101):
        najvecja = max(najvecja, sestej_stevke(a ** b))
        if najvecja == sestej_stevke(a ** b):
            print(a, b)