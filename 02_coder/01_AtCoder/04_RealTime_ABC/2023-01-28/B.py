n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(str(input()))

l = []
for i in range(m):
    l.append(str(input()))

count = 0
for i in s:
    if i[-3:] in l:
        count += 1

print(count)
