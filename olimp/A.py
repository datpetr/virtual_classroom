n, q = map(int, input().split())
s = input()


main_k = []
words = []


for i in range(n):
    main_k.append(ord(s[i]))


main_k.sort()


for i in range(q):
    check = input()
    words.append([])
    for j in range(n):
        words[i].append(ord(check[j]))

    words[i].sort()


for i in range(q):
    if words[i] == main_k:
        print('YES')
    else:
        print('NO')
