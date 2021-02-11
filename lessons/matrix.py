M = int(input("Enter the number of rows:"))  # кол-во строк
N = int(input("Enter the number of columns:"))  # кол-во столбцов
text = input("Your text: ")


x = 0
y = N
matrix = []
out = []


if len(text) == M * N:
    for i in range(M):
        z = list(text[x:y])
        x += N
        y += N
        matrix += [z]

    x = 0
    y = M

    for i in range(M):
        print(matrix[i])

    for i in range(N):
        for j in range(M):
            out += matrix[j][i]

    for i in range(N):
        print(''.join(out[x:y]))
        x += M
        y += M
else:
    print('Your text uncorrect or number of column or strings')
