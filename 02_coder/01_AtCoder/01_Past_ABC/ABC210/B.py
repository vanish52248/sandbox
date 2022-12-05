import sys

n = int(input())
s = list(input())

for i in range(len(s)):
    if s[i] == "0":
        continue
    elif s[i] == "1":
        print("Takahashi" if i % 2 == 0 else "Aoki")
        sys.exit()