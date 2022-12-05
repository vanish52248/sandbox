n = int(input())
min_ = ""
max_ = ""
c = 0

# 11 ~ 99
for i in range(1, n+1):
    min_ += "1"
    max_ += "9"
    
t = 0
for i in range(int(min_), int(max_)+1):
    i = str(i)
    if (int(i[t]) - int(i[t+1])) <= 1:
        c += 1
    t = (t + 1) if (t + 1) <= len(i) else t
print(c % 998244353)