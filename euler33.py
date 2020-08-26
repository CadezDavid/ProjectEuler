import fractions

# def krajsanje(n, m):
#     list = []
#     m = [i for i in str(m)]
#     n = [i for i in str(n)]
#     k = list(set(m).symmetric_difference(n))
#     if min(m, n) / max(m, n) == min(k[0], k[1]) / max(k[0], k[1])
#         list.append([m, n])

def odstrani_skupne(m, n):
    if '0' in str(n):
        return False
    if '0' in str(m):
        return False
    mlist = [stevka for stevka in str(m) if stevka not in str(n)]
    nlist = [stevka for stevka in str(n) if stevka not in str(m)]
    if len(mlist) != 1 or len(nlist) != 1:
        return False
    return int(mlist[0]) / int(nlist[0])

produkt = fractions.Fraction(1, 1)
list = []

for m in range(10, 100):
    for n in range(m + 1, 100):
        if odstrani_skupne(m, n) == m / n:
            list.append([m, n])
            produkt *= fractions.Fraction(m, n)
print(list)
print(fractions.Fraction(produkt))