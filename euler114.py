slovar_moznosti = {0: 1}

def moznosti(dolzina, zadnji=1):
    '''1 - siva in 0 - rdeča'''
    if dolzina <= 0:
        return int(dolzina == 0)
    elif dolzina == 0:
        return moznosti(3, 0) + moznosti(1, 1)
    elif dolzina in slovar_moznosti and zadnji == 1:
        return slovar_moznosti[dolzina]
    elif zadnji == 1:
        slovar_moznosti[dolzina] = moznosti(dolzina - 3, 0) + moznosti(dolzina - 1, 1)
        return slovar_moznosti[dolzina]
    else:
        return moznosti(dolzina - 1, 0) + moznosti(dolzina - 1, 1)