def dni_v_mescu(m, l):
    if m == 2: #če je februar
        if l % 4 == 0:
            if l % 100 == 0:
                if l % 400 == 0:
                    return 29
                return 28
            return 29
        return 28
    else:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            return 31
        else:
            return 30

def leto(l):
    return [dni_v_mescu(m, l) for m in range(1, 13)]

meseci_v_zadnjem_stoletju = list()

for dodatno_leto in range(1,101):
    meseci_v_zadnjem_stoletju += leto(1900 + dodatno_leto)

stevec_nedelj = 0
dan_v_tednu = 1

for mesec in meseci_v_zadnjem_stoletju:
    dan_v_tednu = ( dan_v_tednu + mesec ) % 7 #prvi dan v naslednjem mesecu
    if dan_v_tednu % 7 == 6: #je nedelja?
        stevec_nedelj += 1

print(stevec_nedelj)