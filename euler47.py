def four_distinct(n):
    i = 2
    delitelji = set()
    while len(delitelji) < 5 and i * i <= n:
        if n % i == 0:
            n = n // i
            delitelji.add(i)
            continue
        i += 1
    delitelji.add(n)
    return len(delitelji) == 4


i = 0

rezultat = 0
while rezultat == 0:
    if four_distinct(i) and four_distinct(i + 1) and four_distinct(i + 2) and four_distinct(i + 3):
        rezultat = i
    i += 1