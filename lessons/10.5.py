flag = False


for a in range(1, 1000000000000):
    for b in range(1, 100000000000):
        if ((108 ** a) * (288 ** b)) % (6 ** 440) == 0:
            print(a + b)
            flag = True
            break
    if flag:
        break