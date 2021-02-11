k = []

for i in range(1, 1000):
    if (i % 5 == 1) and (i % 6 == 1) and (i % 7 == 0):
        k.append(i)

k.sort()
print(k[0])
