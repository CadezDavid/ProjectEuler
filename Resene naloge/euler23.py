
def vsota_deliteljev(n):
    vsota = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                vsota += i
            else:
                vsota += i + n // i
        i += 1
    return vsota

def je_abundant(n):
    return vsota_deliteljev(n) > n

seznam_abundant = list()

for stevilo in range(1, 28124):
    if je_abundant(stevilo):
        seznam_abundant.append(stevilo)

so_lahko = set() #so vsota dveh abundant števil

for st1, stevec in zip(seznam_abundant, range(len(seznam_abundant))):
    for st2 in seznam_abundant[:stevec]:
        if st1 + st2 > 28123:
            break
        so_lahko.add(st1 + st2)

sum = 0

for stevilo in range(1, 28124):
    if stevilo not in so_lahko:
        print(stevilo)
        sum += stevilo