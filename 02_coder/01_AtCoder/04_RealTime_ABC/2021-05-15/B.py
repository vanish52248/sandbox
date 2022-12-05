# 最初に 入力するデータの行数の入力を行う
n = int(input())
# 空のリストを作る
list = []

# データの個数分loopさせる
for i in range(n):
    # s は文字列、tは数値として list変数に格納する
    s, t = input().split()
    list.append([int(t), s])

# list変数内のデータを昇順にソートする
list = sorted(list)


print(list[-2][1])
