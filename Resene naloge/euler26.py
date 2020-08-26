def decimalni_zapis(deljenec, delitelj):
    memo = set()
    decimalni_zapis = ''
    while (deljenec, delitelj) not in memo:
        if deljenec % delitelj == 0:
            decimalni_zapis += str(deljenec // delitelj)
            return decimalni_zapis, deljenec, delitelj
        elif deljenec < delitelj:
            decimalni_zapis += '0'
            memo.add((deljenec, delitelj))
            deljenec *= 10
        else:
            decimalni_zapis += str(deljenec // delitelj)
            memo.add((deljenec, delitelj))
            deljenec = deljenec % delitelj * 10
    return decimalni_zapis

# def je_prastevilo(n):
#     if n < 2 or n == 4 or n == 6 or n == 8:
#         return False
#     i = 3
#     while i*i <= n:
#         if n % i == 0 or n % 2 == 0:
#             return False
#         i += 2
#     return True

slovar = dict()
for i in range(2, 1000):
    slovar[i] = len(decimalni_zapis(1, i))

# for stevilo in range(1, 10 ** 6):
#     if len(decimalni_zapis(1, stevilo)) == stevilo:
#         print(stevilo)

print(max(slovar, key=slovar.get))