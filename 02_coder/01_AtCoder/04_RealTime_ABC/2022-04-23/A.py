a, b, c, d, e, f, x = map(int, input().split())
count_t = 0
count_a = 0
temp_t = x
temp_a = x

while True:
    if a+c <= temp_t:
        temp_t -= a+c
        count_t += 1
    else:
        break
    
takahashi = (((a+c)*count_t) * b) + (b-temp_t)
print(takahashi)

while True:
    if d+f <= temp_a:
        temp_a -= d+f
        count_a += 1
    else:
        break
    
aoki = (((d+f)*count_a) * e) + (e-temp_a)
print(aoki)