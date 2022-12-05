s = list(input())
t = list(input())
temp = (ord(s[0]) - ord(t[0])) % 26

def alphabet(s, t):
    for i in range(len(s)):
        if (ord(s[i]) - ord(t[i])) % 26 == temp:
            continue
        else:
            return "No"
    return "Yes"

print(alphabet(s, t))