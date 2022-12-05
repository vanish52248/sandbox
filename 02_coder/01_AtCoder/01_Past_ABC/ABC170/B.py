x, y = map(int,input().split())
if y % 2 == 1:
    print("No")
    exit()
if x * 2 <= y <= x * 4:
    print("Yes")
else:
    print("No")