n, k, x = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)

print(total-(k*x))
