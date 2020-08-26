from itertools import permutations

def je_pandigital(stevilo):
    return len(str(stevilo)) == 9 and len(set(str(stevilo))) == 9 and isinstance(stevilo, int)

def tuple_to_str(tuple):
    string = ''
    for indeks in range(len(tuple)):
        string += str(tuple[indeks])
    return string

seznam_pandigital_st = set([tuple_to_str(tuple) for tuple in permutations('123456789', 9)])

vsota = set()

for stevilo in seznam_pandigital_st:
    if int(stevilo[0]) * int(stevilo[1:5]) == int(stevilo[5:]) or \
        int(stevilo[:2]) * int(stevilo[2:5]) == int(stevilo[5:]) :
        vsota.add(int(stevilo[5:]))