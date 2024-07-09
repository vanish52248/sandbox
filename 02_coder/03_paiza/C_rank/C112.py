n = int(input())

result = []
for i in range(n):
    s, f, t = map(int, input().split())
    result.append(s+f+(24-t))

print(min(result))
print(max(result))
