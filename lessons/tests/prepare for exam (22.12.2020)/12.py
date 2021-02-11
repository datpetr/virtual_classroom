n = int(input())
res = 0

if n % 2 == 0:
    res += 2
    n //= 2
    for i in range(1, n):
        if n % i == 0:
            res += i
            n //= i
else:
    res += 3
    n //= 3
    for i in range(1, n):
        if n % i == 0:
            res += i
            n //= i

print(res - 1)
