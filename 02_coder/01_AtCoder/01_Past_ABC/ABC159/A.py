# 順列 組み合わせ
n, m = map(int, input().split())

even = 0
odd = 0

for i in range(1, n):
    even += i

for i in range(1, m):
    odd += i

print(even+odd)
