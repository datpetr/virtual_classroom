n = int(input())
words = input()


alphabet = '-abcdefghijklmnopqrstuvwxyz'
res = []
k = []
len_word = len(alphabet)


k = ''.join(words).replace(' ', '-')

for i in k:
    res.append(alphabet[(alphabet.find(i) + n) % len_word])


print('result: ', '"', ''.join(res), '"', sep='')
