length, amount = map(int, input().split())

mainNonList = input()
main = []


for i in range(length):
    main.append(ord(mainNonList[i]))


main.sort()
words = []


for i in range(amount):
    wordBuf = input()

    words.append([])

    for y in range(length):
        words[i].append(ord(wordBuf[y]))

    words[i].sort()


for i in range(amount):
    if words[i] == main:
        print("YES")
    else:
        print("NO")
