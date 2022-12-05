from collections import defaultdict

n = int(input())

num = defaultdict(int)

for i in range(n):
    s = "".join(sorted(input()))
    num[s] += 1

# 集計
result = 0
for s in num:
    n = num[s]
    print(n,"----------------")
    result += n * (n - 1) // 2

print(result)
