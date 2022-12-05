x, y, z = map(int, input().split())

if y < x < z:
    print(-1)
elif y < x:
    print(x)
else:
    print(abs(x)+abs(y)+abs(z))
