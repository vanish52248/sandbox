k = int(input())
a, b = map(str, input().split())

a = int(a, base=k)
b = int(b, base=k)

print(a * b)