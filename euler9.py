vsota = []
for n in range(1,100):
    for m in range(n,100):
        if m**2 + m*n == 500:
            vsota.append(m)
            vsota.append(n)

m = vsota[0]
n = vsota[1]
a = m**2 - n**2
b = 2*m*n
c = m**2 + n**2
produkt = a*b*c