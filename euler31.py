kovancki = [200, 100, 50, 20, 10, 5, 2, 1]

def st_moznosti(n, m=0):
    if n == 0 or m == len(kovancki) - 1:
        return 1
    else:
        moznosti = 0
        for stevilo in range(0, n // kovancki[m] + 1):
            moznosti += st_moznosti(n - kovancki[m] * stevilo, m + 1)
        return moznosti