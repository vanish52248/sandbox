s = input()
t = input()

left = 0
for i in range(len(s)):
    if s[i] != t[i]:
        break
    else:
        left += 1

print(left+1)
