k, n = map(int, input().split())

point = 100 / n
scores = []
for _ in range(k):
    current = 0
    d, a = map(int, input().split())
    if d <= 0:
        current = point * a
    elif 1 <= d <= 9:
        current = (point * a) * 0.8
    elif 10 <= d:
        current = 0
    scores.append(current)

for i in scores:
    if 80 <= i <= 100:
        print("A")
    elif 70 <= i <= 79:
        print("B")
    elif 60 <= i <= 69:
        print("C")
    elif 0 <= i <= 59:
        print("D")
