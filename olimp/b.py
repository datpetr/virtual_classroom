from math import factorial as fac


def a(m, n):
    return fac(n) / fac(n - m)


def c(n, k):
    return a(k, n) / fac(k)


numb = int(input())
result = c(numb, 11) * c(numb - 11, 11) / 2


print(int(result % (10 ** 9 + 7)))
