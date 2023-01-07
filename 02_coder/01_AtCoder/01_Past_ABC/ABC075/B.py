h, w = map(int, input().split())

lst = [list(input()) for _ in range(h)]

h_lst = []
w_lst = []

for i in range(h):
    for j in range(w):
        if lst[i][j] == "#":
            h_lst.append(i)
            w_lst.append(j)
        else:
            lst[i][j] = 0

for i, j in zip(h_lst, w_lst):
    if i > 0 and j > 0 and lst[i-1][j-1] != "#":
        lst[i-1][j-1] += 1
    if i > 0 and lst[i-1][j] != "#":
        lst[i-1][j] += 1
    if i > 0 and j < w-1 and lst[i-1][j+1] != "#":
        lst[i-1][j+1] += 1
    if j > 0 and lst[i][j-1] != "#":
        lst[i][j-1] += 1
    if j < w-1 and lst[i][j+1] != "#":
        lst[i][j+1] += 1
    if i < h-1 and j > 0 and lst[i+1][j-1] != "#":
        lst[i+1][j-1] += 1
    if i < h-1 and lst[i+1][j] != "#":
        lst[i+1][j] += 1
    if i < h-1 and j < w-1 and lst[i+1][j+1] != "#":
        lst[i+1][j+1] += 1

for i in lst:
    print("".join(str(i)).replace(", ", "").replace("'", "").replace("[", "").replace("]", ""))
