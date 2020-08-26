a, b = 1, 1
stevec = 2

while a < 10 ** 999 and b < 10 ** 999:
    if a < b:
        a += b
    else:
        b += a
    stevec += 1