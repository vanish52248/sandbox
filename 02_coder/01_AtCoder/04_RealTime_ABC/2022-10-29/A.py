n = int(input())


h = list(map(int, input().split()))

ans = 0
max_ = 0
for i, v in enumerate(h):
    if max_ < v:
        max_ = v
        ans = i + 1

print(ans)
