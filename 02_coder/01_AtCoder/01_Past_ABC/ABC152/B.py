a, b = (input().split())
result = ""

if a < b:
    for i in range(int(b)):
        result += a
else:
    for i in range(int(a)):
        result += b

print(result)