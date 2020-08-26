import itertools

prastevila = [2, 3, 5, 7, 11, 13, 17]

vsota = 0

for pan_st in itertools.permutations(range(10), 10):
    iskana_lastnost = all(
        int(''.join([str(pan_st[k]), str(pan_st[k + 1]), str(pan_st[k + 2])])) % prastevila[k - 1] == 0 for k in range(1, 8)
        )
    if iskana_lastnost and pan_st[0] != 0:
        vsota += int(''.join([str(pan_st[d]) for d in range(10)])) 