n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [False] * n
ep = [False] * n

dp[0] = True
ep[0] = True

for i in range(n-1):
    # print(i,"回目---------------------")
    # print(dp)
    # print(ep)
    if dp[i]:
        if abs(a[i]-a[i+1])<=k:
            dp[i+1] = True
        if abs(a[i]-b[i+1])<=k:
            ep[i+1] = True
    if ep[i]:
        if abs(b[i]-b[i+1])<=k:
            ep[i+1] = True
        if abs(b[i]-a[i+1])<=k:
            dp[i+1] = True
# print("last-----------")
# print(dp)
# print(ep)
print("Yes" if dp[n-1] or ep[n-1] else "No")
