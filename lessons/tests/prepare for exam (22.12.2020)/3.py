k = []
a2 = 0
b2 = 0

for a in range(1000):
    for b in range(1000):
        if a == b:
            if (2 * a + 13) > (b + 7):
                a2 = (2 * a + 13) % (b + 7)
            else:
                b2 = ((b + 7) % (2 * a + 13))
            k.append(a2 + b2)

k.sort()
print(k[-1])
