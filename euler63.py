i = 1
while i < 9 ** (len(str(i))):
    i *= 10

i = i ** (1/2)

stevec = 0

for osnova in range(1, 10):
    n = 1
    while 10 ** ( ( n - 1 ) / ( n ) ) <= osnova:
        stevec += 1
        n += 1