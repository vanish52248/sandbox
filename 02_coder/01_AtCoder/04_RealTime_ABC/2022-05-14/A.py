import copy
s = list(input())
current = copy.copy(s)

while True:
    if len(s) == 6:
        break
    for i in range(len(current)):
            s.append(current[i])
print("".join(s))