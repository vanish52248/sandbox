q = int(input())
a = []
result = []

for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        a.append(query[1])
    elif query[0] == 2:
        a2 = []
        for i in a:
            if query[1] >= i:
                a2.append(i)
                a2.sort(reverse=True)
        if len(a2) >= query[2]:
            result.append(a2[query[2]-1])
        else:
            result.append(-1)
    elif query[0] == 3:
        a3 = []
        for i in a:
            if query[1] <= i:
                a3.append(i)
                a3.sort()
        if len(a3) >= query[2]:
            result.append(a3[query[2]-1])
        else:
            result.append(-1)
            
for i in result:
    print(i)