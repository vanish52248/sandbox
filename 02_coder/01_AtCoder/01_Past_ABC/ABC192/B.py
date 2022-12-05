import re
s = list(input())
f = True

for i in range(len(s)):
    if i % 2 == 0:
        if re.search(r"[a-z]", s[i]):
            f = True
        else:
            f = False
            break
    elif i % 2 == 1:
        if re.search(r"[A-Z]", s[i]):
            f = True
        else:
            f = False
            break
        
print("Yes" if f else "No")