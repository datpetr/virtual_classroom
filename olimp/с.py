amount, request = map(int, input().split())

k = []
tree = []
request_k = []
answer = []
elem = 0
count = 0


for i in range(amount - 1):
    for j in map(str, input().split()):
        k.append(j)
    tree.append(k)
    k = []


for i in map(str, input().split()):
    request_k.append(i)


for i in request_k:
    if i != '1':
        for j in tree:
            if i == j[1]:
                elem = j[0]
                break

        for j in tree:
            if elem == j[0]:
                count += 1

        answer.append(count)
        count = 0
    else:
        answer.append('1')


for i in answer:
    print(i)
