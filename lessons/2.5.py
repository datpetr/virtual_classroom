from math import factorial as fac

count = 0

count += (fac(9) / (fac(9))) + (fac(11) / fac(11))

for i in range(1, 9):
    count += 2 * (fac(10) / (fac(10 - i) * fac(i))) * (fac(10) / (fac(9) * fac(1)))

for i in range(1, 11):
    count += 2 * (fac(12) / (fac(12 - i) * fac(i))) * (fac(12) / (fac(11) * fac(1)))

print(count)
