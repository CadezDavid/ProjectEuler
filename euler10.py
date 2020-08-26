def je_praševilo(stevilo):
	if stevilo < 2:
		return False
	for i in range(2, int(stevilo ** 0.5) + 1):
		if stevilo % i == 0:
			return False
	return True

sum = 0

for stevilo in range(1, 2 * 10 ** 6):
	if je_praševilo(stevilo):
		sum += stevilo