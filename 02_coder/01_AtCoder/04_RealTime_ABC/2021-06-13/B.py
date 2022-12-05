n = int(input())
a = list(map(int, input().split()))
a.sort()
count = []

for i in range(1, n + 1):
    count.append(i)

if count == a:
    print("Yes")
else:
    print("No")