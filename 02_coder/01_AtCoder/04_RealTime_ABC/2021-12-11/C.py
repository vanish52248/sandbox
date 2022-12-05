n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]

for i in range(q):
    cnt = 0
    for j in range(n):
        if x[i] <= a[j] :
            cnt += 1
    print(cnt)
