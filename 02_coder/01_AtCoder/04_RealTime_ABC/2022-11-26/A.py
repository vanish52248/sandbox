s = input()

count = 0
for i in s:
    if i == "v":
        count += 1
    elif i == "w":
        count += 2

print(count)
