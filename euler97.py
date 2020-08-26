i = 28433

for _ in range(1, 7830458):
    i *= 2
    i %= 10**10

i += 1

print(str(i)[-10:])