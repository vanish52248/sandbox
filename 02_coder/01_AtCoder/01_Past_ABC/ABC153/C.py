n, k = map(int, input().split())
h = sorted(list(map(int, input().split())), reverse=True)
count = 0

if n <= k:
    print(0)
    exit()
else:
    for i in range(k):
        h[i] = 0

print(sum(h))