n = int(input())
h = list(map(int, input().split()))

count = 1
first = h[0]
max_ = 0

for i in range(1, n):
    if h[i] >= max_ and h[i] >= first:
        count += 1
        max_ = h[i]

print(count)
