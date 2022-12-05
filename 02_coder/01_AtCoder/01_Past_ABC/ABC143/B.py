from itertools import combinations

n = int(input())
d = list(map(int, input().split()))
result = 0

x = combinations(d, 2)

for i in x:
    result += i[0] * i[1]
    
print(result)