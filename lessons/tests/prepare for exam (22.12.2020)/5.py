for m in range(-1000, 1000):
    if (m % 13 == 8 and m % 15 == 0) and (m // 13 == m // 15):
        print(m)
