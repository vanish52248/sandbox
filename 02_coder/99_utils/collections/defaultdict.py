# ABC237_C
from collections import defaultdict

n = int(input())

# defaultdict(<class 'int'>, {}) を作成する
num = defaultdict(int)

# num[s]: 文字列s が入力値の中に何個あるかカウント
for i in range(n):
    # 文字列をソートして受け取る
    s = "".join(sorted(input()))
    # 文字列が出た回数をインクリメントする
    num[s] += 1

# 3
# acornistnt
# peanutbomb
# constraint
# ↓
# defaultdict(<class 'int'>, {'acinnorstt': 2, 'abbemnoptu': 1})

# 集計
result = 0
for s in num:
    # 文字列 s が n 個ある
    n = num[s]
    
    # nc2 を足していく
    result += n * (n - 1) // 2

# 
print(result)
