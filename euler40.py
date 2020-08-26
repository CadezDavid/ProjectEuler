konstanta = ''
s = 1
while len(konstanta) < 10 ** 6 + 2:
    konstanta += str(s)
    s += 1
produkt = 1
for i in range(1, 7):
    produkt *= int( konstanta[10 ** i - 1] )