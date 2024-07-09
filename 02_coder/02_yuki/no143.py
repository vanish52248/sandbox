k, n, f = map(int, input().split())
a = list(map(int, input().split()))
print((k*n) - sum(a) if (k*n) >= sum(a) else -1)