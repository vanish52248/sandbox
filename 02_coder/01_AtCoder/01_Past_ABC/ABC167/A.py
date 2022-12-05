import re
s = input()
t = input()

pattern = r"[a-zA-z0-9]"

if re.compile(s+pattern).search(t):
    print("Yes")
else:
    print("No")