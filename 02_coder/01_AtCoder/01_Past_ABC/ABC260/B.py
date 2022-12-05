n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
for i in range(x):
    if max(a) == a[i]:
        ans.append(i+1)
        del a[i]
        del b[i]
        break

for i in range(y):
    if max(b) == b[i]:
        ans.append(i+1)
        del a[i]
        del b[i]
        break

count = 0
total = []
for i, v in zip(a, b):
    total.append(i+v)

for i, v in zip(a, b):
    index, count = 0, 0
    if max(total) == i+v:
        ans.append(index)
        count += 1
        del a[index]
        del b[index]
        if count == z:
            break
    index += 1

print(ans)
    