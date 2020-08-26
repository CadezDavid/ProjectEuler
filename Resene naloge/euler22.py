import math
import re
import string


seznam_imen = list(open('euler22.txt'))[0]
seznam_imen = seznam_imen.replace('"','')
seznam_imen = seznam_imen.split(',')
seznam_imen.sort()

vrednosti = dict()
for index, letter in enumerate(string.ascii_uppercase):
   vrednosti[letter] = index + 1

def vrednostimena(ime):
    vsota = 0
    for crka in ime:
        vsota += int(vrednosti[crka])
    return vsota

celotna_vsota = 0

for ime in seznam_imen:
    celotna_vsota += vrednostimena(ime) * (seznam_imen.index(ime) + 1)