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
    max_ = max(num[s], max_)

for s in sorted(num):
    if num[s] == max_:
        print(s)
    

