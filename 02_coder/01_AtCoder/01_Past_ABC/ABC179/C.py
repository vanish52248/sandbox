N = int(input())

ans = 0

# Aに１からN-1までの値を順番に代入して試す
for A in range(1, N):
    # Bに１からN-1までの値を順番に代入して試す
    for B in range(1, N):
        # AとBを固定したとき、Cとしてあり得る数はN-A*Bの１つしかない
        C = N - A * B
        # Cの候補が正の整数であるかどうか調べる
        if C > 0:
            ans += 1
print(ans)