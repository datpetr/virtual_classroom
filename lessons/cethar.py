n = int(input())
words = input()


k = []
k2 = []
answer = []
alphabet = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


for i in words:
    if i == ' ':
        k.append('-')
    else:
        k.append(i)

print(k)


for i in k:
    for j in range(len(i)):
        if i[j] == '-':
            answer.append('-')
        else:
            for el in range(len(alphabet)):
                if i[j] == alphabet[el]:
                    if 0 < el + n < 27:
                        answer.append(alphabet[el + n])
                    else:
                        if (el + n) % 28 >= 0:
                            print((el + n + 1) % 28)
                            answer.append(alphabet[n - (el + n + 1) % 28 - 1])
                        else:
                            answer.append(alphabet[29 + ((el + n) % 28) + 1])


print("result='", end='')


for i in answer:
    print(i, end='')


print("'")
