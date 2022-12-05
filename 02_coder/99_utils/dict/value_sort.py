# ABC142_C

n = int(input())
a = list(map(int, input().split()))

ans = {}
for i, v in enumerate(a, start=1):
    ans[i] = v

# key, value の内valueで昇順でソート
ans = sorted(ans.items(), key=lambda x:x[1])

for i in ans:
    # 改行なしでキーのみを全て出力
    print(i[0], end=" ")