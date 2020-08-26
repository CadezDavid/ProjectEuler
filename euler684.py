def s(n):
    return int( str(n % 9) + ((n // 9) % 1000000007) * '9' )

def veliki_s(n):
    n = n % 1000000007
    if n // 9 > 10:
        prvi_del = int( '4' + (n // 9 - 1) * '9' + '5' )
        drugi_del = int( '8' + (n // 9 - 2) * '9' + '1' )
        tretji_del = sum([s(i) for i in range((n // 9) * 9, n + 1)])
        return prvi_del + drugi_del + tretji_del
    else:
        return sum([s(i) for i in range(n + 1)])

# veliki_s(10000000000)

slovar_fibonacci = {0: 0, 1: 1}

def fibonacci(n):
    if n in slovar_fibonacci:
        return slovar_fibonacci[n]
    else:
        slovar_fibonacci[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return slovar_fibonacci[n]

# vsota = 0
# for i in range(1, 91):
#     vsota += veliki_s(fibonacci(i))