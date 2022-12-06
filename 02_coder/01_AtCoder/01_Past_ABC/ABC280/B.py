n = int(input())
s = list(map(int, input().split()))

a = s[0]
lst = [s[0]]
for i in range(1, n):
    lst.append(s[i] - a)
    a = s[i]

print(*lst)
