n, q = map(int, input().split())
s = input()

# 累積和cs を求める
cs = [0] * (n+1)
print(cs)
for i in range(1, n):
    cs[i+1] = cs[i] + (s[i-1:i+1] == "AC")
    
# 各クエリに応える
for q in range(q):
    # 区間を取得
    l, r = map(int, input().split())
    
    # 右端に1を足して、インデックスを0始まりにする
    l -= 1
    
    # 累積和を用いて答えを求める
    print(cs[r]-cs[l+1])
