for i in range(1, 1000):
    if (i % 4 == 1) and (i % 5 == 1) and ((i + 1) % 6 == 0):
        print(i)
        break
