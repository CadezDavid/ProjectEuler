ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "]

twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]

thousands = ["","thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ", "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ", "novemdecillion ", "vigintillion "]

def num999(n):
    c = n % 10 # singles digit
    b = ((n % 100) - c) / 10 # tens digit
    a = ((n % 1000) - (b * 10) - c) / 100 # hundreds digit
    a, b, c = int(a), int(b), int(c)
    t = ''
    h = ''
    if a != 0 and b == 0 and c == 0:
        t = ones[a] + 'hundred '
    elif a != 0:
        t = ones[a] + 'hundred and '
    if b <= 1:
        h = ones[n%100]
    elif b > 1:
        h = twenties[b] + ones[c]
    st = t + h
    return st

def num2word(num):
    if num == 0:
        return 'zero'
    i = 3
    n = str(num)
    word = ''
    k = 0
    while i == 3:
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = num999(int(nw)) + thousands[int(nw)] + word
        else:
            word = num999(int(nw)) + thousands[k] + word
        if n == '':
            i = i + 1
        k += 1
    return word.lstrip()

def prestej_crke(niz_besed):
    stevec = 0
    for znak in niz_besed:
        if znak != ' ':
            stevec += 1
    return stevec

vsota = 0

for stevilo in range(1, 1001):
    vsota += prestej_crke(num2word(stevilo))