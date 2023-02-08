h, w = map(int, input().split())
r, c = map(int, input().split())

count = 0

if r + 1 <= h:
    count += 1
if r - 1 > 0:
    count += 1
if c + 1 <= w:
    count += 1
if c - 1 > 0:
    count += 1

print(count)
