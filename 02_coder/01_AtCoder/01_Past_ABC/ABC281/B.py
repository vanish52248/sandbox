import re

s = input()

flg = False
try:
    if re.match(r"[A-Z]",s[0]):
        if 10000 <= int(s[1:6])  <= 99999:
            if re.match(r"[A-Z]",s[-1]):
                flg = True
except:
    print("No")
    exit()
        
print("Yes" if flg else "No")
