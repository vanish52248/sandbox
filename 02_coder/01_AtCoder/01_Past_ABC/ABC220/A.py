a, b, c = map(int, input().split())
d = -1

for i in range(a, b+1):
    if i % c == 0:
        d = i
        break

print(d)
