res = 0
k = []
count = 0

for n in range(1, 100000):
    if n % 42 == 0:
        for i in range(1, n):
            if n % i == 0:
                count += 1

        if count == 42:
            k.append(n)

        count = 0

for i in k:
    print(i, end=' ')
