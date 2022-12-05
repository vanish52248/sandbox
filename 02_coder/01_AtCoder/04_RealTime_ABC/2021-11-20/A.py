s, t, x = map(int, input().split())

if((s <= x and x <= t - 1) or (t == 0 and x == 23)):
    print("Yes")
else:
    print("No")
