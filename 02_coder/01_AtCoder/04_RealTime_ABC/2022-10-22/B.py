
# リストを横から縦に変換
h, w = map(int, input().split())

c = [list(input()) for _ in range(h)]
print(c)

l_2d_t = [list(x) for x in zip(*c)]
print(l_2d_t)

for i in range(w):
    count = 0
    for j in range(h):
        if l_2d_t[i][j] == "#":
            count += 1
    print(count, end=" ")
