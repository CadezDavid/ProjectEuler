najvecji = 0

for stevilo1 in range(100, 999):
    for stevilo2 in range(stevilo1, 999):
        if str(stevilo1 * stevilo2) == str(stevilo1 * stevilo2)[::-1]:
            najvecji = max(stevilo1 * stevilo2, najvecji)