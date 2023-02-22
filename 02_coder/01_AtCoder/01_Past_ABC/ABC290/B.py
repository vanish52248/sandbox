n, k = map(int, input().split())
s = input()

count = 0
lst = []
for i in s:
    if i == "o":
        if count >= k:
            lst.append("x")
        else:
            lst.append("o")
            count += 1
    else:
        lst.append("x")

print(("").join(lst))
