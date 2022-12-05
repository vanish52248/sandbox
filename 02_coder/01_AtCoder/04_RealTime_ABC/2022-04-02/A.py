from collections import Counter

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x_lst = [x1, x2, x3]
y_lst = [y1, y2, y3]

x = (Counter(x_lst).most_common()[-1][0])
y = (Counter(y_lst).most_common()[-1][0])

print(x, y)
