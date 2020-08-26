def match(n):
    s = str(n)
    return not all(int(s[x*2]) == x+1 for x in range(9))

n = 138902663
while match(n*n):
    n -= 2

print("Project Euler 206 Solution =", n*10)