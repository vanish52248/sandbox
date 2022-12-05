n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

row = [False] * n
for i in (a):
    row[i-1] = True

for i in range(q):    
    count = 0
    for j in range(len(row)):
        if row[j]:
            count += 1
        if count == l[i]:
            if j != len(row)-1 and row[j+1]==False:
                row[j] = False
                row[j+1] = True
                break

ans = []
for i, v in enumerate(row):
    if v:
        ans.append(i+1)

print(*ans)