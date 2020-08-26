def je_palindrom(n):
    return str(n) == str(n)[::-1]

def je_lychrelova(n):
    'Ne postane palindrom.'
    stevec = 0
    while stevec < 50:
        n = n + int(str(n)[::-1])
        if je_palindrom(n):
            return False
        stevec += 1
    return True

stevec = 0

for stevilo in range(1, 10 ** 4):
    if je_lychrelova(stevilo):
        stevec += 1