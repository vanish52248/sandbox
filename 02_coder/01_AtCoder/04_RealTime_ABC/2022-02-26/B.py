import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(m):
    if b[i] in a:
        a.remove(b[i])
        continue
    else:
        print("No")
        sys.exit()

print("Yes")