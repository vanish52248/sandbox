s = input()
t = input()

ans = len(t)
if t in s:
    print(0)
    exit()
else:
    for i in range(len(t)):
        count = 0
        for j in range(len(t)):
            current += t[j]
            if current in s:
                count -= 1
            
            
print(count)