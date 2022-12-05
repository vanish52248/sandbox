n = int(input())
a = list(map(int, input().split()))

ans = {}
for i, v in enumerate(a, start=1):
    ans[i] = v

ans = sorted(ans.items(), key=lambda x:x[1])

for i in ans:
    print(i[0], end=" ")