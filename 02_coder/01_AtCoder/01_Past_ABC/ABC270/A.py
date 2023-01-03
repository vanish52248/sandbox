a, b = map(int, input().split())

q = [False] * 3

if a in [1, 3, 5, 7] or b in [1, 3, 5, 7]:
    q[0] = True

if a in [2, 3, 6, 7] or b in [2, 3, 6, 7]:
    q[1] = True

if a in [4, 5, 6, 7] or b in [4, 5, 6, 7]:
    q[2] = True

ans = 0
for i in range(len(q)):
    if i == 0 and q[i]:
        ans += 1
    elif i == 1 and q[i]:
        ans += 2
    elif i == 2 and q[i]:
        ans += 4

print(ans)
