n, t = map(int, input().split())
a = list(map(int, input().split()))

dp = t

for i in range(n-1):
    # print("-----------")
    # print(a[i]+t, a[i+1])
    if a[i] + t < a[i+1]:
        dp += t
    else:
        dp += a[i+1] - a[i]
    # print(dp)
print(dp)    
    