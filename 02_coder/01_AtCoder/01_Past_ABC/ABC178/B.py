a, b, c, d = map(int, input().split())
# 答えが負になることもあるため負の無限大数 infで設定
t = -float('inf')

for i in (a, b):
    for j in (c, d):
        t = max(t, i*j)


print(t)