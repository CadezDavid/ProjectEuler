import math

def to_binary(n):
    binarni_zapis = ''
    potenca = math.floor(math.log(n, 2)) + 1
    while potenca > 0:
        if n >= 2 ** (potenca - 1):
            binarni_zapis += '1'
            n -= 2 ** (potenca - 1)
        else:
            binarni_zapis += '0'
        potenca -= 1
    return binarni_zapis

def palindrome(n):
    return str(n) == str(n)[::-1]

palindromi = set()

for stevilo in range(1, 1000):
    palindrom = str(stevilo)[::-1] + str(stevilo)
    if palindrome(to_binary(int(palindrom))):
        palindromi.add(int(palindrom))
    palindrom = str(stevilo) + str(stevilo)[::-1]
    if palindrome(to_binary(int(palindrom))):
        palindromi.add(int(palindrom))

for stevilo in range(0, 100):
    for vmesno_stevilo in range(0, 10):
        palindrom = str(stevilo)[::-1] + str(vmesno_stevilo) + str(stevilo)
        if stevilo == vmesno_stevilo == 0:
            break
        if palindrome(to_binary(int(palindrom))):
            palindromi.add(int(palindrom))
        palindrom = str(stevilo)[::-1] + str(vmesno_stevilo) + str(stevilo)
        if palindrome(to_binary(int(palindrom))):
            palindromi.add(int(palindrom))

for i in range(1, 10):
    if palindrome(to_binary(i)):
        palindromi.add(i)

print(palindromi)
print(sum(palindromi))
print(len(palindromi))