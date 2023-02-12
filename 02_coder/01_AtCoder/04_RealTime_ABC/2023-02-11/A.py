s = input()

temp = ""
for i in s:
    if i == "0":
        temp += "1"
    elif i == "1":
        temp += "0"
print(temp)
