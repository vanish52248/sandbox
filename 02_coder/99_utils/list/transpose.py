# ABC237_B
# 配列を横持ちのデータから縦持ちに変更するやり方

# 4 3
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12

transpose = []
# 行列の一つ目の要素を取得し、その個数分ループ処理
for i in range(len(a[0])):
    tmp = []
    # 行列要素のインデックスを利用して作成された
    # tmpリストをさらにリストに追加していくことで転置された行列を作成
    for j in a:
        tmp.append(j[i])
    transpose.append(tmp)
    
for i in transpose:
    print(*i)
    # 1 4 7 10
    # 2 5 8 11
    # 3 6 9 12