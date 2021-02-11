n = int(input())
words = input()


alphabet = 'abcdefghijklmnopqrstuvwxyz'
res = []
len_word = len(alphabet)


for i in words:
    if i == ' ':
        res.append('-')
    else:
        res.append(alphabet[(alphabet.find(i) + n) % len_word])


print('result: ', '"', ''.join(res), '"', sep='')
