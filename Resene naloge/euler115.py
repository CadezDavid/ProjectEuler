slovar_moznosti = {0: 1}

def moznosti(dolzina, zadnji=1, m=3):
    '''1 - siva in 0 - rdeča'''
    if dolzina <= 0:
        return int(dolzina == 0)
    elif dolzina == 0:
        return moznosti(m, 0, m) + moznosti(1, 1, m)
    elif (dolzina, m) in slovar_moznosti and zadnji == 1:
        return slovar_moznosti[(dolzina, m)]
    elif zadnji == 1:
        slovar_moznosti[(dolzina, m)] = moznosti(dolzina - m, 0, m) + moznosti(dolzina - 1, 1, m)
        return slovar_moznosti[(dolzina, m)]
    else:
        return moznosti(dolzina - 1, 0, m) + moznosti(dolzina - 1, 1, m)

vrednost = 0
i = 50
while vrednost < 10 ** 6:
    i += 1
    vrednost = moznosti(i, 1, 50)