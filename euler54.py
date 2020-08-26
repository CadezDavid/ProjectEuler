import random
import collections
from itertools import combinations

def nov_kup():
    kup = list()
    barve = ['H', 'D', 'S', 'C']
    karte = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for barva in barve:
        for karta in karte:
            kup += [(karta,barva)]
    return kup

slovar = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def premesaj(karte):
    random.shuffle(karte)

def razdeli_karte(igralci, karte):
    premesaj(karte)
    slovar = dict()
    for igralec in igralci:
        slovar[igralec] = [karte.pop(), karte.pop()]
    return slovar

def odpri_skupne_karte(karte):
    skupne_karte = list()
    for _ in range(5):
        skupne_karte += [karte.pop()]
    return skupne_karte

def na_dva_dela(karte):
    return ([i[0] for i in karte], [i[1] for i in karte])

def tvorijo_lestvico(karte):
    seznam = range(min(na_dva_dela(karte)[0]), max(na_dva_dela(karte)[0]) + 1)
    for i in seznam:
        if not i in na_dva_dela(karte)[0]:
            return False
    return True

def kolikokrat_se_pojavi_katera_stevilka(karte):
    return dict(collections.Counter(na_dva_dela(karte)[0]))

def vrednost(peterka):
    if set(na_dva_dela(peterka)[0]) == {10, 11, 12, 13, 14} and len(set(na_dva_dela(peterka)[1])) == 1:
        return 9
    elif tvorijo_lestvico(peterka) and len(set(na_dva_dela(peterka)[1])) == 1:
        return 8
    elif set(kolikokrat_se_pojavi_katera_stevilka(peterka).values()) == {4, 1}:
        return 7
    elif set(kolikokrat_se_pojavi_katera_stevilka(peterka).values()) == {3, 2}:
        return 6
    elif len(set(na_dva_dela(peterka)[1])) == 1:
        return 5
    elif 3 in set(kolikokrat_se_pojavi_katera_stevilka(peterka).values()):
        return 4
    elif list(kolikokrat_se_pojavi_katera_stevilka(peterka).values()).count(2) == 2:
        return 3
    elif 2 in kolikokrat_se_pojavi_katera_stevilka(peterka).values():
        return 2
    else:
        return 1

def ovrednoti(karte):
    return max([vrednost(kombinacija) for kombinacija in combinations(karte, 5)])

def poker(imena):
    karte = nov_kup()
    premesaj(karte)
    slovar_igralcev = razdeli_karte(imena, karte)
    skupne_karte = odpri_skupne_karte(karte)
    slovar_igralcev_tocke = dict()
    for igralec in slovar_igralcev:
        slovar_igralcev_tocke[igralec] = ovrednoti(slovar_igralcev[igralec] + skupne_karte)
    print(skupne_karte)
    for oseba in sorted( slovar_igralcev.keys() ):
        print('{} {} {}'.format(oseba, ovrednoti(skupne_karte + slovar_igralcev[oseba]), slovar_igralcev[oseba]))

prvi_zmagal = 0

seznam_kart = list()
with open('euler54.txt') as karte:
    for runda in karte.readlines():
        runda = runda.replace('\n', '').split(' ')
        runda = [(slovar.get(a), b) for a, b in runda]
        seznam_kart.append((runda[:5], runda[5:]))
        # if vrednost(runda[:5]) > vrednost(runda[5:]):
        #     prvi_zmagal += 1
        # elif vrednost(runda[:5]) == vrednost(runda[5:]) and vrednost(runda[:5]) == 1:
        #     prve = sorted(na_dva_dela(runda[:5])[0])
        #     druge = sorted(na_dva_dela(runda[5:])[0])
        #     while prve[-1] == druge[-1]:
        #         prve.pop()
        #         druge.pop()
        #     if prve[-1] > druge[-1]:
        #         prvi_zmagal += 1

for igra in seznam_kart:
    prve_karte = igra[0]
    druge_karte = igra[1]
    if vrednost(prve_karte) != vrednost(druge_karte):
        if vrednost(prve_karte) > vrednost(druge_karte):
            prvi_zmagal += 1
    elif vrednost(prve_karte) == 2:
        a = na_dva_dela(prve_karte)[0][0:]
        b = na_dva_dela(druge_karte)[0][0:]
        for i in set(na_dva_dela(prve_karte)[0]):
            a.remove(i)
        for i in set(na_dva_dela(druge_karte)[0]):
            b.remove(i)
        if max(a) > max(b):
            prvi_zmagal += 1
        elif max(a) == max(b):
            c = na_dva_dela(prve_karte)[0][0:]
            e = na_dva_dela(druge_karte)[0][0:]
            if c > e:
                prvi_zmagal += 1
    elif vrednost(prve_karte) == 1:
        a = sorted(na_dva_dela(prve_karte)[0])
        b = sorted(na_dva_dela(druge_karte)[0])
        if a > b:
            prvi_zmagal += 1
    elif vrednost(prve_karte) == 3:
        a = na_dva_dela(prve_karte)[0][0:]
        b = na_dva_dela(druge_karte)[0][0:]
        for i in set(na_dva_dela(prve_karte)[0]):
            a.remove(i)
        for i in set(na_dva_dela(druge_karte)[0]):
            b.remove(i)
        if a > b:
            prvi_zmagal += 1