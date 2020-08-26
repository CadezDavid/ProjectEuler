def is_prime(n):
    n = int(n)
    if n < 2:
         return False
    if n % 2 == 0:
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def f(n):
    s = 1
    p = 2
    while p <= n:
        if is_prime(s):
            p *= s
        s += 2
    return int(p / (s - 2))