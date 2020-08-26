import statistics

n = input("Stevilka")

def trikotniki(x):
    list = []
    for a in range(1, int(x) // 2):
        for b in range(a, int(x) // 2):
            if ( ( a ** 2 + b ** 2 ) ** (1/2) ) % 1 == 0 and \
            a + b + ( ( a ** 2 + b ** 2 ) ** (1/2) )  < int(x) :
                c = int( (a ** 2 + b ** 2 ) ** (1/2) )
                trojica = {a, b, c}
                if trojica not in list:
                    list.append(trojica)
                else:
                    pass
    return list

obsegi = []

for i in trikotniki(n):
    obsegi.append(sum(i))

print(trikotniki(n))
print(obsegi)
print(statistics.mode(obsegi))
