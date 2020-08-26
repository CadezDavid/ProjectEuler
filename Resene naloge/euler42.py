import string
import math

slovar = {crka: vrednost for vrednost, crka in enumerate(string.ascii_uppercase, 1)}
besede = open('euler42.txt', 'r')
sez_besed = [beseda.replace('"', '') for beseda in besede.read().split(',')]

def vrednost_besede(beseda):
    vsota = 0
    for crka in beseda:
        vsota += slovar[crka]
    return vsota

def je_trikotnisko_stevilo(n):
    return float(math.floor(math.sqrt(1 + 8 * n))) == float(math.sqrt(1 + 8 * n)) and \
    int(math.floor(math.sqrt(1 + 8 * n))) % 2 == 1

stevec = 0
with open('euler42.txt', 'r') as besede:
    seznam_besed = [beseda.replace('"', '') for beseda in besede.read().split(',')]
    for beseda in seznam_besed:
        if je_trikotnisko_stevilo(vrednost_besede(beseda)):
            stevec += 1