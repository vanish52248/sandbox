n = int(input())

s = [list(input()) for _ in range(n)]

end = ""
for i, v in enumerate(s):
    if i == 0:
        end = v[-1]
        continue
    else:
        if end != v[0]:
            print(end, v[0])
            exit()
        end = v[-1]
print("Yes")
