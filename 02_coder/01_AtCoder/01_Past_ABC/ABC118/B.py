n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

for i in a:
    del i[0]

ans = []
for i in range(len(a)):
    for j in range(len(a[i])):
        flg = True
        for v, k in enumerate(a):
            if not flg or a[i][j] not in k:
                flg = False
                continue
            if flg and v == len(a)-1 and a[i][j] not in ans:
                ans.append(a[i][j])

print(len(ans))

            
            
