n = int(input())
w = list(map(int, input().split()))
min_weight = 100
for i in range(1, n+1):
    s1 = 0
    s2 = 0
    for j in range(1, n+1):    
        if j <= i:
            s1 += w[j-1]
        else:
            s2 += w[j-1]
    min_weight = min(min_weight, (abs(s1-s2)))

print(min_weight)