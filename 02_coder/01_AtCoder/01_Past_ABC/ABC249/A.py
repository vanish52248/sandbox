a, b, c, d, e, f, x = map(int, input().split())

t_count = 0
current = x
while(True):
    if current > a:
        current -= a
        t_count += (a*b)
        current -= c
    elif current <= a and current > 0:
        t_count += (current*b)
        break
    else:
        break

a_count = 0
current = x
while(True):
    if current > d:
        current -= d
        a_count += (d*e)
        current -= f
    elif current <= d and current > 0:
        a_count += (current*e)
        break
    else:
        break

print("Takahashi" if t_count > a_count else "Aoki" if t_count < a_count else "Draw")