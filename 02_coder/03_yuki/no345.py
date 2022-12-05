s = input()
count = 0
temp = 0
current = ""
for i in range(1, len(s)+1):
    if s[i-1] == "c" and current == "":
        temp = i
        current += "c"
    elif s[i-1] == "w" and current == "c":
        current += "w"
    elif s[i-1] == "w" and current == "cw":
        current += "w"
        temp = (i - temp + 1)
    
print(temp if current == "cww" else -1)
    