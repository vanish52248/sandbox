import re

s = list(input())
c = 0

for i in range(len(s)):
    if re.compile(r'[0-9]').search(s[i]):
        c += int(s[i])
        
print(c)