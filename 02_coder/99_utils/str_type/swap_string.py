# ABC221_B
# 文字列を1文字ずつ持つ配列をそれぞれ用意
s = list(input())
t = list(input())
if s == t:
        print("Yes")
        exit()
else:
    for i in range(len(s)-1):
        # まず隣の文字と入れ替える（それ以外の文字列はそのまま）
        # ①abc -> bac
        s[i], s[i+1] = s[i+1], s[i]
        # 入れ替えた文字列配列と配列tが一致したら"Yes"
        if s == t:
            print("Yes")
            exit()
        # 比較して一致しなかったら入れ替えた文字を元に戻す
        # ②bac -> abc
        s[i], s[i+1] = s[i+1], s[i]
# 最後まで一致しなかったら"No"
print("No")