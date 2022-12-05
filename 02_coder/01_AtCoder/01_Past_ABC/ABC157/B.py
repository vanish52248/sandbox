# BINGOゲーム ３＊３マス
flg = [[False, False, False], [False, False, False], [False, False, False]]
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
n = int(input())

for i in range(n):
    t = 0
    b = int(input())
    if b in a1:
        t = a1.index(b)
        flg[0][t] = True
    elif b in a2:
        t = a2.index(b)
        flg[1][t] = True
    elif b in a3:
        t = a3.index(b)
        flg[2][t] = True
        
if (flg[0].count(True) == 3) or (flg[1].count(True) == 3) or (flg[2].count(True) == 3):
    print("Yes")
elif (flg[0][0] and flg[1][0] and flg[2][0]) or (flg[0][1] and flg[1][1] and flg[2][1]) or (flg[0][2] and flg[1][2] and flg[2][2]):
    print("Yes")
elif (flg[0][0] and flg[1][1] and flg[2][2]) or (flg[0][2] and flg[1][1] and flg[2][0]):
    print("Yes")
else:
    print("No")