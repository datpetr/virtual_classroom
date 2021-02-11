s = input().split()

k = []
k2 = []
result = []
flag = True

n = int(s[0])
q = int(s[1])


for i in range(q + 1):
    k.append(ord(input()))


s = k[0]

for i in s:
    k2.append(i)


for i in range(1, 1 + q):
    for j in k2:
        if j not in k[i]:
            flag = False
            break
        else:
            continue
    if flag:
        result.append('YES')
    else:
        result.append('NO')
    flag = True


for i in result:
    print(i)
