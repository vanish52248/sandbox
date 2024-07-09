n, m = map(int, input().split())
max_ = 0

score = []
for _ in range(m):
    score.append(int(input()))

for i in range(n):
    current = 100
    for j in range(m):
        h = int(input())
        if abs(score[j] - h) <= 5:
            current -= 0
        elif abs(score[j] - h) <= 10:
            current -= 1
        elif abs(score[j] - h) <= 20:
            current -= 2
        elif abs(score[j] - h) <= 30:
            current -= 3
        else:
            current -= 5
        if j + 1 == m:
            max_ = max(max_, current)
            break
        
print(max_)