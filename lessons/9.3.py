flag = True


for a in range(1, 10000):
    if flag:
        for b in range(1, 10000):
            if flag:
                for c in range(1, 10000):
                    if flag:
                        for d in range(1, 10000):
                            if flag:
                                for e in range(1, 10000):
                                    if (a + b + c + d + e == 12) and (a ** 2 + b ** 2 + c ** 2 + d ** 2 + e ** 2 == 32):
                                        print(a, b, c, d, e)
                                        flag = False
                                        break