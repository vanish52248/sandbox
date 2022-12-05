x, a, d, n = map(int, input().split())
s = [a]
i = 0
ans_1 = 0
ans_2 = 0

while True:
    if len(s) == n:
        break
    else:
        s.append(s[i]+d)
    i += 1

if x in s:
    print(0)
    exit()

operation = 0
current = x
max_s = max(s)
# +1
while True:    
    if current in s:
        ans_1 = operation
        break
    else:
        current += 1
        operation += 1
    if current >= max_s:
        ans_1 = float('inf')
        break

operation = 0
current = x
min_s = min(s)
# -1
while True:    
    if current in s:
        ans_2 = operation
        break
    else:
        current -= 1
        operation += 1
    if current <= min_s:
        ans_2 = float('inf')
        break

print(min(ans_1, ans_2))