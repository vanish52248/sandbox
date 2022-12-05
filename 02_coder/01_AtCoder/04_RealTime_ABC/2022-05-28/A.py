a, b, c = map(int, input().split())
lst = []

lst.append(a)
lst.append(b)
lst.append(c)
lst.sort()

print("Yes" if lst[1] == b else "No")