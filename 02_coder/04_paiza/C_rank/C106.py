# 入力値の受け取り
N = int(input())
scores = list(map(int, input().split()))

# 大きい順に並べ替え→リストに戻す
tmp = list(reversed(sorted(scores)))

# 答えを格納する辞書を作る
dicts = {key:"" for key in tmp}

# メダルを渡す処理
# 大きい順に回せるのでちょっと楽
cnt = 0
for i in tmp:
    # 今回調査する点数が授与済みの場合は何もしない
    if dicts[i]:
        pass
    else:
        # 一人も受け取ってなければ金
        if cnt == 0:
            dicts[i] = "G"
        # 一人だけ受け取っている場合は銀
        elif cnt == 1:
            dicts[i] = "S"
        # 二人だけ受け取っている場合は銅
        elif cnt == 2:
            dicts[i] = "B"
        # それ以外は授与なし
        else:
            dicts[i] = "N"
        # 渡した人数をカウントしてループの頭に戻る
        cnt += scores.count(i)

# 出力        
for i in scores:
    print(dicts[i])
