# ABC245_C
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 初期値（配列）
dp = [False] * n
ep = [False] * n
# 初期値の頭だけTrueにするdp,ep配列を用意する
dp[0] = True
ep[0] = True

for i in range(n-1):
    print(i,"回目---------------------")
    print(dp)
    print(ep)    
    # A側の i が Trueなら判定(その手前は判定しない)
    if dp[i]:
        if abs(a[i]-a[i+1])<=k:
            dp[i+1] = True
        if abs(a[i]-b[i+1])<=k:
            ep[i+1] = True
    # B側の i が Trueなら判定(その手前は判定しない)
    if ep[i]:
        if abs(b[i]-b[i+1])<=k:
            ep[i+1] = True
        if abs(b[i]-a[i+1])<=k:
            dp[i+1] = True
print("last-----------")
print(dp)
print(ep)

# 配列の最後の数がTrueならそこまで来てるという証拠だからその2つで判定
print("Yes" if dp[n-1] or ep[n-1] else "No")
