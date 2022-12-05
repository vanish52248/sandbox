W, a, b = map(int, input().split())
if a + W < b:
    print(b-(W+a))
elif b + W < a:
    print(a-(W+b))
else:
    print(0)