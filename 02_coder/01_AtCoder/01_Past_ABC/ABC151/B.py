# 標準入力としてn, k, m受け取る
n, k, m = map(int, input().split())
# 現在のn-1科目の点数を受け取って合計する
a = sum(map(int, input().split()))

# 科目数*平均点-現在の合計点が満点以下なら0か平均点を出力
if n * m - a <= k:
    print(max(n * m - a, 0))
# 科目数*平均点-現在の合計点が満点より上なら -1 を出力
else:
    print(-1)
