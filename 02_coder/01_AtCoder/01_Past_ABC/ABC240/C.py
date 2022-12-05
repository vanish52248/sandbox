import sys
N, X = map(int, input().split())
temp = 0

for i in range(N):
    a, b = map(int, input().split())
    if temp > X:
        print("No")
        sys.exit()
    elif (temp+a) > X:
        temp += b
    elif (temp+b) > X:
        temp += a
    else:
        temp += max(a, b)
print("Yes" if temp == X else "No")
    