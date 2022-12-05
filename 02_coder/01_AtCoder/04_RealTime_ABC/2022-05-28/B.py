h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
x = 0
y = 0
lst = []

for i in range(h):
    for j in range(w):
        if s[i][j] == "o":
            x = j+1
            y = i+1
            lst.append(x)
            lst.append(y)
    
if lst[0] == lst[2]:
    print(abs(lst[1]-lst[3]))
else:
    print(abs(lst[1]-lst[3])+abs(lst[0]-lst[2]))