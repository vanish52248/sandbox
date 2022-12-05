s, t, x = map(int, input().split())

if (s < x < t) or (t < s <= x) or (x < t < s):
    print("Yes")
else:
    print("No")