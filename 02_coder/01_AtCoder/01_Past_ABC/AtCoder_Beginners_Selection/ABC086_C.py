n = int(input())
i = 0
flg = True
for _ in range(n):
    t, x, y = map(int, input().split())
    if x + y > abs(t - i):
        flg = False
    i = t
print("Yes" if flg else "No")