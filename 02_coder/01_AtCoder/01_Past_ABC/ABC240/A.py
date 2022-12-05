a, b = map(int, input().split())

if a == 1:
    print("Yes" if b == 10 else "Yes" if b-a == 1 else "No")
else:
    print("Yes" if b-a == 1 else "No")
