s = input()

count = 0
result = 0
for i in s:
    if i == "A" or i == "C" or i == "G" or i == "T":
        count += 1
        result = max(count, result)
    else:
        result = max(count, result)
        count = 0

print(result)
