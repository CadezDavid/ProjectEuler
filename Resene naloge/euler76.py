slovar = dict()

def moznosti(stevilo, dolzina):
    if (stevilo, dolzina) in slovar:
        return slovar[(stevilo, dolzina)]
    elif stevilo <= 0 or dolzina <= 0:
        return int(stevilo == dolzina == 0)
    else:
        slovar[(stevilo, dolzina)] = moznosti(stevilo - 1, dolzina - 1) + moznosti(stevilo - dolzina, dolzina)
        return slovar[(stevilo, dolzina)]

def vse_moznosti(stevilo):
    return sum([moznosti(stevilo, dolzina) for dolzina in range(2, stevilo + 1)])