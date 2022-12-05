h, w = map(int, input().split())
a = []
min_ = 101
c = 0

for i in range(h):
    a.append(list(map(int, input().split())))

for i in range(h):
    for j in range(w):
        min_ = min(min_, a[i][j])
        
for i in range(h):
    for j in range(w):
        if a[i][j] == min_:
            continue
        else:
            c += abs(min_ - a[i][j])

print(c)