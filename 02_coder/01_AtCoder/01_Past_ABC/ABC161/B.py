n, m = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)

a.sort(reverse=True)

for i in range(m):
    if a[i] >= total * (1/(m*4)):
        continue
    else:
        print("No")
        exit()
print("Yes")