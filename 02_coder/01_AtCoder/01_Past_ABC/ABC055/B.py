n = int(input())
m = 10**9+7
c = 1

for i in range(1, n+1):
    c *= i
    c %= m
print(c)