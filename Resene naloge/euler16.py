n = int(input("Potenca 2:"))

def vsota_stevk(n):
    stevilo = 2 ** n
    stevilo = str(stevilo)
    vsota = 0
    for stevka in stevilo:
        vsota += int(stevka)
    return vsota

print(vsota_stevk(n))