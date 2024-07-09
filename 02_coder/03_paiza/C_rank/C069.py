y, m, d = map(int, input().split())
a, b = map(int, input().split())

# 開催年
year = y+1
while True:
    if year % 4 == 1:
        break
    year += 1

year2 = year - y
# 当月の残日数
result = (15-d) if m % 2 == 0 else (13-d)

# その年の残日数
for i in range(m+1, 14):
    if i % 2 == 0:
        result += 15
    else:
        result += 13
    

# 対象年の日数
result += b


days = (13*7) + (15*6)
if year2 > 1:
    result += days * (year2-1)
    for i in range(1, a):
        if i % 2 == 0:
            result += 15
        else:
            result += 13
    result +=  (15-b) if a % 2 == 0 else (13-b)
print(result)
