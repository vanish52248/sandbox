a, b, c, d = map(int, input().split())

if b < c or d < a:
    print(0)
else:
    print(abs(max(a,c)-min(b,d)))