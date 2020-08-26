seznam_stevilk = map(int, list(map(str.strip, list(open('euler13.txt','r')))))

vsota = sum([int(i) for i in seznam_stevilk])

print(str(vsota)[0:10])