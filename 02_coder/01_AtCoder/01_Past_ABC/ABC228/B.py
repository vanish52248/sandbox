n, x = map(int, input().split())
Ai = list(map(int, input().split()))
check = [False for i in range(n)]
current = x - 1
count = 0

# FalseならループさせてTrueなら処理終了させる
while not check[current]:
    check[current] = True
    count += 1
    current = Ai[current] - 1
print(count)
