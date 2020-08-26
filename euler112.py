def bouncy(stevilo):
    if stevilo < 100:
        return False
    return not (sorted(str(stevilo), reverse=False) == list(str(stevilo)) or sorted(str(stevilo), reverse=True) == list(str(stevilo)))

bouncy_stevil = 0
stevilo = 1
while 100 * bouncy_stevil < 99 * stevilo:
    if bouncy(stevilo):
        bouncy_stevil += 1
    stevilo += 1