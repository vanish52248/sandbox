import re

s = list(input())

flg = False
if s[0] != "A":
    print("WA")
    exit()
else:
    for i in range(len(s)):
        if s[i] == "C" and (2 <= i <= len(s)-2):
            s.remove("C")
            break
    else:
        print("WA")
        exit()
s.remove("A")

if re.search('[A-Z]', ("").join(s)) is None:
    print("AC")
else:
    print("WA")
