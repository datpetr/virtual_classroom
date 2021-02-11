k1 = []
k2 =[]


for k in range(1, 25):
    for s in range(1, 21):
        if 14 * k == 111 - s:
            k1.append(k)
            k1.append(s)
            k2.append(k1)
            k1 = []
k2.sort()
print(k2[-1])