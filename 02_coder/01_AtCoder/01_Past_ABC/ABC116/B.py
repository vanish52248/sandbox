def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

s = int(input())
ans = []
i = 1
while(True):
    s = f(s)
    if s in ans:
        i += 1
        break
    else:
        i += 1
        ans.append(s)
        
print(i)
