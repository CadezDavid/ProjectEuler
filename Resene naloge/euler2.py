n = input("Do katere stevilke naj gre:")
list = [1]

def fibonaci(n):
    a = 1
    b = 2
    h = 0
    while max(a, b) <= int(n):
        if h % 2 == 0:
            list.append(b)
            a = a + b
            h = h + 1
        else:
            list.append(a)
            b = a + b
            h = h + 1
    return list

def vsotasodih(k):
    t = 0
    k = fibonaci(k)
    for x in k:
        if x % 2 == 0:
            t = t + x
        else:
            pass
    return t

print(fibonaci(n))
print(vsotasodih(n))