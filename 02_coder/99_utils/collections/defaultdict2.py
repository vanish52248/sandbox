# ABC155_C
from collections import defaultdict

n = int(input())

# defaultdict(<class 'int'>, {}) を作成する
num = defaultdict(int)
max_ = 0
# num[s]: 文字列s が入力値の中に何個あるかカウント
for i in range(n):
    # 文字列をソートして受け取る
    s = input()
    # 文字列が出た回数をインクリメントする
    num[s] += 1
    # ループの中で出てきた回数が最大のものを設定する
    max_ = max(num[s], max_)

# 辞書順でソートした文字列をループして、最大数出てきた文字列を出力する
for s in sorted(num):
    if num[s] == max_:
        print(s)
    

