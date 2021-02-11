def coat(s):
    table = [[' '] * n for _ in range(m)]
    k = 0

    for i in range(m):
        for j in range(n):
            table[i][j] = s[k]
            k += 1
            if k == len(s):
                break

    k = 0
    chars = ['\0'] * (m * n)

    for j in range(n):
        for i in range(m):
            chars[k] = table[i][j]
            k += 1
    return ''.join(chars).replace(' ', '_')


m, n = map(int, input('Input amount strings and amount of column (across space): ').split())
strings = input('Input strings: ')


if m * n == len(strings):
    print(coat(strings))
else:
    print('You entered incorrect data')
