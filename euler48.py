def zadnjih_deset(n):
    return int(str(n)[-10:])

s = 0
for i in range(1, 1000):
    s += zadnjih_deset( i ** i )
    s = int(str(s)[-10::])

print(s)