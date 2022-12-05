n, k = map(int, input().split())

# 10進数(N)をK進数に変換するには、NをKで割っていき、あまりを書いていく方法がある。
ans = 0
#NをKで割ったときに切り捨てとした商が0より大きくなるような回数が桁数になる。
while 0 < n:
    n //= k
    ans += 1
print(ans)
