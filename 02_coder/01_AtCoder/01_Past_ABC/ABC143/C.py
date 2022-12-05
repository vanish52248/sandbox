n = int(input())
s = input()

lst = []
for i in range(len(s)):
    if i == len(s)-1:
        lst.append(s[i])
        break
    if s[i] != s[i+1]:
        lst.append(s[i])
 
print(len(lst))