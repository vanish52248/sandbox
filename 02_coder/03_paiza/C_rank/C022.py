n = int(input())

s = [list(map(int, input().split())) for _ in range(n)]

ans = [s[0][0], s[n-1][1]]
min_ = 100000
max_ = 0
for i in s:
    max_ = max(max_, i[2])
    min_ = min(min_, i[3])
    
ans.append(max_)
ans.append(min_)

print(*ans)
