a, b = map(int, input().split())

if (a == b):
    print("Draw")
elif a == 1 and b > 1:
    print("Alice")
elif a > 1 and b == 1:
    print("Bob")
else:
    print("Alice" if a > b else "Bob")